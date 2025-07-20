from django.urls import path
from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from .views import (
    register, login, login_success, dashboard, students, teachers, subjects, home, class_page, class_detail,
    reports_dashboard, logbook_list, logbook_create, logbook_detail, logbook_edit, logbook_submit, logbook_review,
    workplan_list, workplan_create, workplan_detail, workplan_edit, workplan_submit, workplan_review
)

def logout_view(request):
    logout(request)
    return redirect('login')

urlpatterns = [
    path('', home, name='home'),  # Make home the default page after login
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('login-success/', login_success, name='login_success'),
    path('dashboard/', dashboard, name='dashboard'),
    path('students/', students, name='students'),
    path('teachers/', teachers, name='teachers'),
    path('subjects/', subjects, name='subjects'),
    path('success/', lambda request: render(request, 'account/success.html'), name='success'),
    path('class/', class_page, name='class'),
    path('class/<int:class_id>/', class_detail, name='class_detail'),
    
    # Reports System URLs
    path('reports/', reports_dashboard, name='reports_dashboard'),
    
    # Logbook URLs
    path('reports/logbooks/', logbook_list, name='logbook_list'),
    path('reports/logbooks/create/', logbook_create, name='logbook_create'),
    path('reports/logbooks/<int:logbook_id>/', logbook_detail, name='logbook_detail'),
    path('reports/logbooks/<int:logbook_id>/edit/', logbook_edit, name='logbook_edit'),
    path('reports/logbooks/<int:logbook_id>/submit/', logbook_submit, name='logbook_submit'),
    path('reports/logbooks/<int:logbook_id>/review/', logbook_review, name='logbook_review'),
    
    # Workplan URLs
    path('reports/workplans/', workplan_list, name='workplan_list'),
    path('reports/workplans/create/', workplan_create, name='workplan_create'),
    path('reports/workplans/<int:workplan_id>/', workplan_detail, name='workplan_detail'),
    path('reports/workplans/<int:workplan_id>/edit/', workplan_edit, name='workplan_edit'),
    path('reports/workplans/<int:workplan_id>/submit/', workplan_submit, name='workplan_submit'),
    path('reports/workplans/<int:workplan_id>/review/', workplan_review, name='workplan_review'),
]
