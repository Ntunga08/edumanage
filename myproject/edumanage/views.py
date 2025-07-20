from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count, Q
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import User, Class, Student, StudentClass, Subject, Exam, Result

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Log the user in immediately after registration
            return redirect('success') # Redirect to dashboard
    else:
        form = CustomUserCreationForm()

    return render(request, 'account/register.html', {'form': form})

def login(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = CustomAuthenticationForm()
    
    return render(request, 'account/login.html', {'form': form})

def login_success(request):
    return render(request, 'account/login_success.html')

@login_required
def dashboard(request):
    user = request.user
    
    # Get real statistics from database
    total_students = Student.objects.filter(is_active=True).count()
    total_classes = Class.objects.filter(is_active=True).count()
    total_teachers = User.objects.filter(classes__isnull=False).distinct().count()
    total_subjects = Subject.objects.filter(is_active=True).count()
    
    # Get all classes and their students
    classes = Class.objects.filter(is_active=True).order_by('name')
    class_student_map = []
    for c in classes:
        students = StudentClass.objects.filter(class_obj=c, is_active=True).select_related('student')
        class_student_map.append({
            'class': c,
            'students': [
                {'name': s.student.full_name, 'student_id': s.student.student_id}
                for s in students
            ]
        })
    
    context = {
        'user_name': user.username,
        'user_initials': user.username[0].upper() if user.username else 'U',
        'school_name': 'EduManage Academy',
        'class_student_map': class_student_map,
        'total_students': total_students,
        'total_classes': total_classes,
        'total_teachers': total_teachers,
        'total_subjects': total_subjects,
    }
    return render(request, 'dashboard.html', context)

@login_required
def students(request):
    user = request.user
    all_students = Student.objects.filter(is_active=True)
    total = all_students.count()
    classes = Class.objects.all().order_by('name')
    context = {
        'user_name': user.username,
        'user_initials': user.username[0].upper() if user.username else 'U',
        'school_name': 'EduManage Academy',
        'total_students': total,
        'classes': classes,
    }
    return render(request, 'student.html', context)

@login_required
def teachers(request):
    user = request.user
    # Get all unique teacher names from Class
    teacher_names = Class.objects.exclude(teacher='').values_list('teacher', flat=True).distinct()
    teachers_data = []
    for name in teacher_names:
        classes = Class.objects.filter(teacher=name)
        class_list = []
        total_students = 0
        for c in classes:
            student_count = c.current_students_count
            class_list.append({
                'class_name': c.full_name,
                'subject': c.name,
                'student_count': student_count,
            })
            total_students += student_count
        teachers_data.append({
            'name': name,
            'classes': class_list,
            'total_students': total_students,
        })
    context = {
        'user_name': user.username,
        'user_initials': user.username[0].upper() if user.username else 'U',
        'school_name': 'EduManage Academy',
        'teachers_data': teachers_data,
    }
    return render(request, 'teachers.html', context)

@login_required
def subjects(request):
    user = request.user
    all_subjects = Subject.objects.filter(is_active=True).order_by('name')
    total = all_subjects.count()
    
    # Get class count for each subject
    subjects_data = []
    for subject in all_subjects:
        class_count = subject.classes.count()
        subjects_data.append({
            'subject': subject,
            'class_count': class_count,
        })
    
    context = {
        'user_name': user.username,
        'user_initials': user.username[0].upper() if user.username else 'U',
        'school_name': 'EduManage Academy',
        'total_subjects': total,
        'subjects': subjects_data,
    }
    return render(request, 'subjects.html', context)

@login_required
def home(request):
    user = request.user
    context = {
        'user_name': user.username,
        'user_initials': user.username[0].upper() if user.username else 'U',
        'school_name': 'EduManage Academy',
    }
    return render(request, 'home.html', context)

@login_required
def class_page(request):
    user = request.user
    # Get classes where the current user is the teacher
    teacher_classes = Class.objects.filter(teacher=user, is_active=True).prefetch_related('subjects')
    
    # Prepare class data with student counts and recent results
    classes_data = []
    for class_obj in teacher_classes:
        # Get students in this class
        students = StudentClass.objects.filter(class_obj=class_obj, is_active=True).select_related('student')
        
        # Get recent exams for this class
        recent_exams = Exam.objects.filter(class_obj=class_obj, is_active=True).order_by('-exam_date')[:3]
        
        # Calculate average performance for each exam
        exam_performance = []
        for exam in recent_exams:
            results = Result.objects.filter(exam=exam)
            if results.exists():
                avg_marks = results.aggregate(Avg('marks_obtained'))['marks_obtained__avg']
                avg_percentage = (avg_marks / exam.total_marks) * 100 if exam.total_marks > 0 else 0
                exam_performance.append({
                    'exam': exam,
                    'avg_percentage': round(avg_percentage, 1),
                    'total_students': results.count()
                })
        
        # Count students by gender
        male_count = students.filter(student__gender='M').count()
        female_count = students.filter(student__gender='F').count()
        
        classes_data.append({
            'class': class_obj,
            'total_students': students.count(),
            'male_students': male_count,
            'female_students': female_count,
            'subjects': class_obj.subjects.all(),
            'recent_exams': recent_exams,
            'exam_performance': exam_performance,
            'room': class_obj.room_number or 'TBD',
            'level': f"Grade {class_obj.grade} - Section {class_obj.section}",
            'code': f"{class_obj.grade}{class_obj.section}"
        })
    
    context = {
        'user_name': user.username,
        'user_initials': user.username[0].upper() if user.username else 'U',
        'school_name': 'EduManage Academy',
        'classes': classes_data,
    }
    return render(request, 'class.html', context)

@login_required
def class_detail(request, class_id):
    user = request.user
    class_obj = get_object_or_404(Class, id=class_id, teacher=user)
    
    # Get all students in this class
    student_enrollments = StudentClass.objects.filter(class_obj=class_obj, is_active=True).select_related('student')
    students = [enrollment.student for enrollment in student_enrollments]
    
    # Get all exams for this class
    exams = Exam.objects.filter(class_obj=class_obj, is_active=True).order_by('-exam_date')
    
    # Get results for all students in this class
    student_results = {}
    for student in students:
        student_results[student.id] = {
            'student': student,
            'results': Result.objects.filter(student=student, exam__class_obj=class_obj).select_related('exam', 'exam__subject')
        }
    
    # Calculate class statistics
    total_students = len(students)
    male_count = len([s for s in students if s.gender == 'M'])
    female_count = len([s for s in students if s.gender == 'F'])
    
    # Calculate overall class performance
    all_results = Result.objects.filter(exam__class_obj=class_obj)
    if all_results.exists():
        overall_avg = all_results.aggregate(Avg('marks_obtained'))['marks_obtained__avg']
        overall_percentage = (overall_avg / 100) * 100  # Assuming 100 is max marks
    else:
        overall_avg = 0
        overall_percentage = 0
    
    context = {
        'user_name': user.username,
        'user_initials': user.username[0].upper() if user.username else 'U',
        'school_name': 'EduManage Academy',
        'class_obj': class_obj,
        'students': students,
        'exams': exams,
        'student_results': student_results,
        'total_students': total_students,
        'male_count': male_count,
        'female_count': female_count,
        'overall_avg': round(overall_avg, 1),
        'overall_percentage': round(overall_percentage, 1),
    }
    return render(request, 'class_detail.html', context)
