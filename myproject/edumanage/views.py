from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import User, Class, Student, StudentClass

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
            return redirect('dashboard')
    else:
        form = CustomAuthenticationForm()
    
    return render(request, 'account/login.html', {'form': form})

def login_success(request):
    return render(request, 'account/login_success.html')

@login_required
def dashboard(request):
    user = request.user
    # Get all classes and their students
    classes = Class.objects.all().order_by('name')
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
    }
    return render(request, '.html', context)

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
def home(request):
    user = request.user
    context = {
        'user_name': user.username,
        'user_initials': user.username[0].upper() if user.username else 'U',
        'school_name': 'EduManage Academy',
    }
    return render(request, 'home.html', context)
