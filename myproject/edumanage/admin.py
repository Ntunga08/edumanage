from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Class, Student, StudentClass

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # Use the default UserAdmin configuration and add any customizations here
    # The default UserAdmin already includes fields like:
    # list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    # search_fields = ('username', 'first_name', 'last_name', 'email')
    # list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    pass

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'name', 'teacher', 'room_number', 'current_students_count', 'capacity', 'available_seats', 'academic_year', 'is_active']
    list_filter = ['grade', 'section', 'academic_year', 'is_active']
    search_fields = ['name', 'teacher', 'room_number']
    ordering = ['grade', 'section']
    readonly_fields = ['current_students_count', 'available_seats']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'grade', 'section', 'academic_year')
        }),
        ('Capacity & Teacher', {
            'fields': ('capacity', 'teacher', 'room_number')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('Statistics', {
            'fields': ('current_students_count', 'available_seats'),
            'classes': ('collapse',)
        }),
    )
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('studentclass_set')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'full_name', 'age', 'gender', 'parent_name', 'enrollment_date', 'is_active']
    list_filter = ['gender', 'enrollment_date', 'is_active']
    search_fields = ['student_id', 'first_name', 'last_name', 'parent_name', 'email']
    ordering = ['first_name', 'last_name']
    readonly_fields = ['age', 'enrollment_date']
    
    fieldsets = (
        ('Student Information', {
            'fields': ('student_id', 'first_name', 'last_name', 'date_of_birth', 'gender', 'email', 'phone', 'address')
        }),
        ('Parent Information', {
            'fields': ('parent_name', 'parent_phone', 'parent_email')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('System Information', {
            'fields': ('enrollment_date', 'age'),
            'classes': ('collapse',)
        }),
    )

@admin.register(StudentClass)
class StudentClassAdmin(admin.ModelAdmin):
    list_display = ['student', 'class_obj', 'enrollment_date', 'is_active']
    list_filter = ['class_obj__grade', 'class_obj__section', 'enrollment_date', 'is_active']
    search_fields = ['student__first_name', 'student__last_name', 'student__student_id', 'class_obj__name']
    ordering = ['-enrollment_date']
    readonly_fields = ['enrollment_date']
    
    autocomplete_fields = ['student', 'class_obj']
    
    fieldsets = (
        ('Enrollment', {
            'fields': ('student', 'class_obj')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('System Information', {
            'fields': ('enrollment_date',),
            'classes': ('collapse',)
        }),
    )
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('student', 'class_obj')
