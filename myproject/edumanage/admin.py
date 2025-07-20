from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Class, Student, StudentClass, Subject, Exam, Result, TeacherLogbook, TeacherWorkplan

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # Use the default UserAdmin configuration and add any customizations here
    # The default UserAdmin already includes fields like:
    # list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    # search_fields = ('username', 'first_name', 'last_name', 'email')
    # list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    pass

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'code', 'description']
    ordering = ['name']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'name', 'teacher', 'room_number', 'current_students_count', 'capacity', 'available_seats', 'academic_year', 'is_active']
    list_filter = ['grade', 'section', 'academic_year', 'is_active']
    search_fields = ['name', 'teacher', 'room_number']
    ordering = ['grade', 'section']
    readonly_fields = ['current_students_count', 'available_seats']
    filter_horizontal = ['subjects']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'grade', 'section', 'academic_year')
        }),
        ('Capacity & Teacher', {
            'fields': ('capacity', 'teacher', 'room_number')
        }),
        ('Subjects', {
            'fields': ('subjects',)
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

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ['name', 'exam_type', 'subject', 'class_obj', 'total_marks', 'exam_date', 'is_active']
    list_filter = ['exam_type', 'exam_date', 'is_active', 'subject', 'class_obj__grade']
    search_fields = ['name', 'subject__name', 'class_obj__name']
    ordering = ['-exam_date']
    readonly_fields = ['created_at', 'updated_at']
    
    autocomplete_fields = ['subject', 'class_obj']
    
    fieldsets = (
        ('Exam Information', {
            'fields': ('name', 'exam_type', 'subject', 'class_obj', 'total_marks', 'exam_date')
        }),
        ('Description', {
            'fields': ('description',)
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('System Information', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['student', 'exam', 'marks_obtained', 'percentage', 'grade', 'created_at']
    list_filter = ['exam__exam_type', 'exam__subject', 'exam__class_obj__grade', 'created_at']
    search_fields = ['student__first_name', 'student__last_name', 'student__student_id', 'exam__name']
    ordering = ['-created_at']
    readonly_fields = ['percentage', 'grade', 'created_at', 'updated_at']
    
    autocomplete_fields = ['student', 'exam']
    
    fieldsets = (
        ('Result Information', {
            'fields': ('student', 'exam', 'marks_obtained')
        }),
        ('Remarks', {
            'fields': ('remarks',)
        }),
        ('Calculated Fields', {
            'fields': ('percentage', 'grade'),
            'classes': ('collapse',)
        }),
        ('System Information', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

# Reports System Admin
@admin.register(TeacherLogbook)
class TeacherLogbookAdmin(admin.ModelAdmin):
    list_display = ['teacher', 'subject', 'class_obj', 'report_type', 'report_date', 'status', 'created_at']
    list_filter = ['report_type', 'status', 'report_date', 'academic_year', 'term', 'subject', 'class_obj__grade']
    search_fields = ['teacher__first_name', 'teacher__last_name', 'teacher__email', 'subject__name', 'class_obj__name']
    ordering = ['-report_date', '-created_at']
    readonly_fields = ['created_at', 'updated_at', 'submitted_at', 'reviewed_at']
    
    autocomplete_fields = ['teacher', 'subject', 'class_obj', 'submitted_to', 'reviewed_by']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('teacher', 'subject', 'class_obj', 'report_type', 'report_date', 'academic_year', 'term')
        }),
        ('Content', {
            'fields': ('topics_covered', 'activities_conducted', 'student_participation', 'challenges_faced', 'solutions_implemented', 'next_lesson_plan', 'additional_notes')
        }),
        ('Status & Review', {
            'fields': ('status', 'submitted_to', 'submitted_at', 'reviewed_by', 'reviewed_at', 'review_comments')
        }),
        ('System Information', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('teacher', 'subject', 'class_obj', 'submitted_to', 'reviewed_by')

@admin.register(TeacherWorkplan)
class TeacherWorkplanAdmin(admin.ModelAdmin):
    list_display = ['teacher', 'subject', 'class_obj', 'plan_type', 'academic_year', 'term', 'status', 'created_at']
    list_filter = ['plan_type', 'status', 'academic_year', 'term', 'subject', 'class_obj__grade']
    search_fields = ['teacher__first_name', 'teacher__last_name', 'teacher__email', 'subject__name', 'class_obj__name']
    ordering = ['-created_at']
    readonly_fields = ['created_at', 'updated_at', 'submitted_at', 'reviewed_at']
    
    autocomplete_fields = ['teacher', 'subject', 'class_obj', 'submitted_to', 'reviewed_by']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('teacher', 'subject', 'class_obj', 'plan_type', 'academic_year', 'term')
        }),
        ('Planning Content', {
            'fields': ('learning_objectives', 'topics_to_cover', 'teaching_methods', 'assessment_methods', 'resources_needed', 'timeline')
        }),
        ('End of Term Analysis', {
            'fields': ('achievements', 'challenges_encountered', 'solutions_applied', 'student_performance_analysis', 'recommendations'),
            'classes': ('collapse',)
        }),
        ('Status & Review', {
            'fields': ('status', 'submitted_to', 'submitted_at', 'reviewed_by', 'reviewed_at', 'review_comments')
        }),
        ('System Information', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('teacher', 'subject', 'class_obj', 'submitted_to', 'reviewed_by')
