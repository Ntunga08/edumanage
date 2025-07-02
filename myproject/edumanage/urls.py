from django.urls import path
from django.shortcuts import render
from .views import register, login, login_success, dashboard, students, teachers, home

urlpatterns = [
    path('', home, name='home'),  # Make home the default page after login
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('login-success/', login_success, name='login_success'),
    path('dashboard/', dashboard, name='dashboard'),
    path('students/', students, name='students'),
    path('teachers/', teachers, name='teachers'),
    path('success/', lambda request: render(request, 'account/success.html'), name='success')
]
