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

# New Models for Reports System
class TeacherLogbook(models.Model):
    REPORT_TYPE_CHOICES = [
        ('daily', 'Daily Report'),
        ('weekly', 'Weekly Report'),
        ('monthly', 'Monthly Report'),
    ]
    
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('reviewed', 'Reviewed'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='logbooks')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='logbooks')
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='logbooks')
    report_type = models.CharField(max_length=20, choices=REPORT_TYPE_CHOICES, default='daily')
    report_date = models.DateField()
    academic_year = models.CharField(max_length=9, default="2024-2025")
    term = models.CharField(max_length=20, default="Term 1")
    
    # Content fields
    topics_covered = models.TextField(help_text="Topics covered in this period")
    activities_conducted = models.TextField(help_text="Activities and exercises conducted")
    student_participation = models.TextField(help_text="Student participation and engagement")
    challenges_faced = models.TextField(help_text="Challenges or problems encountered")
    solutions_implemented = models.TextField(help_text="Solutions or strategies implemented")
    next_lesson_plan = models.TextField(help_text="Plan for next lesson/period")
    additional_notes = models.TextField(blank=True, help_text="Any additional notes or observations")

    # New fields for PDF upload and generation
    pdf_upload = models.FileField(upload_to='logbooks/uploaded/', blank=True, null=True, help_text="Upload a PDF of your logbook (optional)")
    generated_pdf = models.FileField(upload_to='logbooks/generated/', blank=True, null=True, help_text="System-generated PDF of your logbook (auto-filled)")
    
    # Status and approval
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    submitted_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='received_logbooks')
    submitted_at = models.DateTimeField(null=True, blank=True)
    reviewed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='reviewed_logbooks')
    reviewed_at = models.DateTimeField(null=True, blank=True)
    review_comments = models.TextField(blank=True, help_text="Comments from academic master")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-report_date', '-created_at']
        verbose_name_plural = "Teacher Logbooks"

    def __str__(self):
        return f"{self.teacher.get_full_name()} - {self.subject.name} ({self.class_obj.full_name}) - {self.report_date}"

class TeacherWorkplan(models.Model):
    PLAN_TYPE_CHOICES = [
        ('beginning_term', 'Beginning of Term'),
        ('end_term', 'End of Term'),
        ('mid_term', 'Mid Term'),
    ]
    
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('reviewed', 'Reviewed'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workplans')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='workplans')
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='workplans')
    plan_type = models.CharField(max_length=20, choices=PLAN_TYPE_CHOICES)
    academic_year = models.CharField(max_length=9, default="2024-2025")
    term = models.CharField(max_length=20, default="Term 1")
    
    # Content fields
    learning_objectives = models.TextField(help_text="Learning objectives for the term")
    topics_to_cover = models.TextField(help_text="Topics to be covered during the term")
    teaching_methods = models.TextField(help_text="Teaching methods and strategies to be used")
    assessment_methods = models.TextField(help_text="Assessment methods and evaluation criteria")
    resources_needed = models.TextField(help_text="Resources and materials needed")
    timeline = models.TextField(help_text="Timeline and schedule for topics")
    
    # For end of term reports
    achievements = models.TextField(blank=True, help_text="Achievements and successes (for end of term)")
    challenges_encountered = models.TextField(blank=True, help_text="Challenges and problems encountered (for end of term)")
    solutions_applied = models.TextField(blank=True, help_text="Solutions and strategies applied (for end of term)")
    student_performance_analysis = models.TextField(blank=True, help_text="Analysis of student performance (for end of term)")
    recommendations = models.TextField(blank=True, help_text="Recommendations for improvement (for end of term)")
    
    # Status and approval
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    submitted_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='received_workplans')
    submitted_at = models.DateTimeField(null=True, blank=True)
    reviewed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='reviewed_workplans')
    reviewed_at = models.DateTimeField(null=True, blank=True)
    review_comments = models.TextField(blank=True, help_text="Comments from academic master")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Teacher Workplans"

    def __str__(self):
        return f"{self.teacher.get_full_name()} - {self.subject.name} ({self.class_obj.full_name}) - {self.get_plan_type_display()}"
