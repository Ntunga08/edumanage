from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    # Django's AbstractUser already includes:
    # username, first_name, last_name, email, password, is_staff, is_active, date_joined
    # We can add any additional fields here if needed.
    # For now, we will use the default fields.
    
    # We will use 'email' as the unique identifier for login instead of 'username'.
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username'] # 'email' is already required by USERNAME_FIELD

    def __str__(self):
        return self.email

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text="Subject name")
    code = models.CharField(max_length=10, unique=True, help_text="Subject code")
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.code})"

class Class(models.Model):
    GRADE_CHOICES = [
        ('I', 'FORM I'),
        ('II', 'FORM II'),
        ('III', 'FORM III'),
        ('IV', 'FORM IV'),
        ('v', 'FORM V'),
        ('VI', 'FORM VI'),
    ]
    
    SECTION_CHOICES = [
        ('A', 'Section A'),
        ('B', 'Section B'),
        ('C', 'Section C'),
        ('D', 'Section D'),
        ('E', 'Section E'),
    ]
    
    name = models.CharField(max_length=100, help_text="e.g., Mathematics, Science, English")
    grade = models.CharField(max_length=3, choices=GRADE_CHOICES)
    section = models.CharField(max_length=1, choices=SECTION_CHOICES)
    capacity = models.PositiveIntegerField(default=30, help_text="Maximum number of students")
    teacher = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, blank=True, related_name='classes', help_text="Assigned teacher")
    subjects = models.ManyToManyField(Subject, related_name='classes', blank=True)
    room_number = models.CharField(max_length=10, blank=True)
    academic_year = models.CharField(max_length=9, default="2024-2025", help_text="e.g., 2024-2025")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['grade', 'section', 'academic_year']
        verbose_name_plural = "Classes"

    def __str__(self):
        return f"Grade {self.grade} - Section {self.section} ({self.name})"
    
    @property
    def full_name(self):
        return f"Grade {self.grade} - Section {self.section}"
    
    @property
    def current_students_count(self):
        return self.studentclass_set.filter(is_active=True).count()
    
    @property
    def available_seats(self):
        return self.capacity - self.current_students_count

class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    student_id = models.CharField(max_length=20, unique=True, help_text="Student ID number")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    parent_name = models.CharField(max_length=100, blank=True)
    parent_phone = models.CharField(max_length=15, blank=True)
    parent_email = models.EmailField(blank=True)
    enrollment_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['first_name', 'last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.student_id})"
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def age(self):
        from datetime import date
        today = date.today()
        return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))

class StudentClass(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['student', 'class_obj']
        verbose_name_plural = "Student Classes"

    def __str__(self):
        return f"{self.student.full_name} - {self.class_obj.full_name}"
    
    def save(self, *args, **kwargs):
        # Check if class has available seats
        if self.is_active and self.class_obj.current_students_count >= self.class_obj.capacity:
            raise ValueError(f"Class {self.class_obj.full_name} is at full capacity")
        super().save(*args, **kwargs)

class Exam(models.Model):
    EXAM_TYPE_CHOICES = [
        ('midterm', 'Midterm'),
        ('final', 'Final'),
        ('quiz', 'Quiz'),
        ('assignment', 'Assignment'),
        ('project', 'Project'),
    ]
    
    name = models.CharField(max_length=100, help_text="Exam name")
    exam_type = models.CharField(max_length=20, choices=EXAM_TYPE_CHOICES)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='exams')
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='exams')
    total_marks = models.PositiveIntegerField(default=100, help_text="Total marks for this exam")
    exam_date = models.DateField()
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-exam_date']
        unique_together = ['name', 'subject', 'class_obj', 'exam_date']

    def __str__(self):
        return f"{self.name} - {self.subject.name} ({self.class_obj.full_name})"

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='results')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='results')
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2, help_text="Marks obtained by student")
    remarks = models.TextField(blank=True, help_text="Teacher remarks")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['student', 'exam']
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.student.full_name} - {self.exam.name} ({self.marks_obtained}/{self.exam.total_marks})"
    
    @property
    def percentage(self):
        if self.exam.total_marks > 0:
            return (self.marks_obtained / self.exam.total_marks) * 100
        return 0
    
    @property
    def grade(self):
        percentage = self.percentage
        if percentage >= 90:
            return 'A+'
        elif percentage >= 80:
            return 'A'
        elif percentage >= 70:
            return 'B+'
        elif percentage >= 60:
            return 'B'
        elif percentage >= 50:
            return 'C+'
        elif percentage >= 40:
            return 'C'
        elif percentage >= 30:
            return 'D'
        else:
            return 'F'
