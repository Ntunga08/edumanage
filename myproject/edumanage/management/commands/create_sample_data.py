from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from edumanage.models import Subject, Class, Student, StudentClass, Exam, Result
from datetime import date, timedelta
import random

User = get_user_model()

class Command(BaseCommand):
    help = 'Create sample data for testing class features'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')

        # Create subjects
        subjects_data = [
            {'name': 'Mathematics', 'code': 'MATH'},
            {'name': 'English', 'code': 'ENG'},
            {'name': 'Science', 'code': 'SCI'},
            {'name': 'History', 'code': 'HIST'},
            {'name': 'Geography', 'code': 'GEO'},
        ]
        
        subjects = []
        for subject_data in subjects_data:
            subject, created = Subject.objects.get_or_create(
                name=subject_data['name'],
                defaults={'code': subject_data['code']}
            )
            subjects.append(subject)
            if created:
                self.stdout.write(f'Created subject: {subject.name}')

        # Create a teacher user if not exists
        teacher, created = User.objects.get_or_create(
            username='teacher1',
            defaults={
                'email': 'teacher1@school.com',
                'first_name': 'John',
                'last_name': 'Smith',
                'is_staff': True
            }
        )
        if created:
            teacher.set_password('password123')
            teacher.save()
            self.stdout.write(f'Created teacher: {teacher.username}')

        # Create classes
        classes_data = [
            {'name': 'Mathematics Class', 'grade': 'I', 'section': 'A', 'room_number': '101'},
            {'name': 'English Class', 'grade': 'II', 'section': 'B', 'room_number': '102'},
            {'name': 'Science Class', 'grade': 'III', 'section': 'A', 'room_number': '103'},
        ]
        
        classes = []
        for class_data in classes_data:
            class_obj, created = Class.objects.get_or_create(
                grade=class_data['grade'],
                section=class_data['section'],
                defaults={
                    'name': class_data['name'],
                    'teacher': teacher,
                    'room_number': class_data['room_number'],
                    'capacity': 30
                }
            )
            if created:
                # Add subjects to class
                class_obj.subjects.add(*subjects[:3])  # Add first 3 subjects
                classes.append(class_obj)
                self.stdout.write(f'Created class: {class_obj.name}')

        # Create students
        students_data = [
            {'first_name': 'Alice', 'last_name': 'Johnson', 'student_id': 'ST001', 'gender': 'F'},
            {'first_name': 'Bob', 'last_name': 'Williams', 'student_id': 'ST002', 'gender': 'M'},
            {'first_name': 'Carol', 'last_name': 'Brown', 'student_id': 'ST003', 'gender': 'F'},
            {'first_name': 'David', 'last_name': 'Jones', 'student_id': 'ST004', 'gender': 'M'},
            {'first_name': 'Eva', 'last_name': 'Garcia', 'student_id': 'ST005', 'gender': 'F'},
            {'first_name': 'Frank', 'last_name': 'Miller', 'student_id': 'ST006', 'gender': 'M'},
        ]
        
        students = []
        for student_data in students_data:
            student, created = Student.objects.get_or_create(
                student_id=student_data['student_id'],
                defaults={
                    'first_name': student_data['first_name'],
                    'last_name': student_data['last_name'],
                    'gender': student_data['gender'],
                    'date_of_birth': date(2010, 1, 1)  # Default DOB
                }
            )
            students.append(student)
            if created:
                self.stdout.write(f'Created student: {student.full_name}')

        # Enroll students in classes
        for class_obj in classes:
            for student in students[:4]:  # Enroll first 4 students in each class
                enrollment, created = StudentClass.objects.get_or_create(
                    student=student,
                    class_obj=class_obj,
                    defaults={'is_active': True}
                )
                if created:
                    self.stdout.write(f'Enrolled {student.full_name} in {class_obj.name}')

        # Create exams
        exam_types = ['midterm', 'final', 'quiz']
        for class_obj in classes:
            for i, subject in enumerate(class_obj.subjects.all()):
                for j, exam_type in enumerate(exam_types):
                    exam_date = date.today() - timedelta(days=30 * (j + 1))
                    exam, created = Exam.objects.get_or_create(
                        name=f'{exam_type.title()} {subject.name}',
                        subject=subject,
                        class_obj=class_obj,
                        defaults={
                            'exam_type': exam_type,
                            'total_marks': 100,
                            'exam_date': exam_date,
                            'description': f'{exam_type.title()} exam for {subject.name}'
                        }
                    )
                    if created:
                        self.stdout.write(f'Created exam: {exam.name}')

        # Create results
        for class_obj in classes:
            students_in_class = StudentClass.objects.filter(class_obj=class_obj, is_active=True).select_related('student')
            exams_in_class = Exam.objects.filter(class_obj=class_obj)
            
            for student_enrollment in students_in_class:
                student = student_enrollment.student
                for exam in exams_in_class:
                    # Generate random marks between 60 and 95
                    marks = random.randint(60, 95)
                    result, created = Result.objects.get_or_create(
                        student=student,
                        exam=exam,
                        defaults={
                            'marks_obtained': marks,
                            'remarks': f'Good performance in {exam.name}'
                        }
                    )
                    if created:
                        self.stdout.write(f'Created result: {student.full_name} - {exam.name}: {marks}/100')

        self.stdout.write(self.style.SUCCESS('Sample data created successfully!'))
        self.stdout.write(f'Created {len(subjects)} subjects')
        self.stdout.write(f'Created {len(classes)} classes')
        self.stdout.write(f'Created {len(students)} students')
        self.stdout.write('Teacher username: teacher1, password: password123') 