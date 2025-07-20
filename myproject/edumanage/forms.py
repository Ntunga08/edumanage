from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, TeacherLogbook, TeacherWorkplan

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email') # Specify the fields to display on the registration form

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'input-field w-full px-3 lg:px-4 py-2.5 lg:py-3 rounded-xl text-sm focus:outline-none transition-all duration-300',
                'placeholder': f'Enter your {field.label.lower()}'
            })

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'input-field w-full px-3 lg:px-4 py-2.5 lg:py-3 rounded-xl text-sm focus:outline-none transition-all duration-300',
            'placeholder': 'Enter your email address'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'input-field w-full px-3 lg:px-4 py-2.5 lg:py-3 rounded-xl text-sm focus:outline-none transition-all duration-300',
            'placeholder': 'Enter your password'
        })

# Forms for Reports System
class TeacherLogbookForm(forms.ModelForm):
    class Meta:
        model = TeacherLogbook
        fields = [
            'subject', 'class_obj', 'report_type', 'report_date', 'academic_year', 'term',
            'topics_covered', 'activities_conducted', 'student_participation', 
            'challenges_faced', 'solutions_implemented', 'next_lesson_plan', 'additional_notes'
        ]
        widgets = {
            'report_date': forms.DateInput(attrs={'type': 'date'}),
            'topics_covered': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Describe the topics covered in this period...'}),
            'activities_conducted': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Describe the activities and exercises conducted...'}),
            'student_participation': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Describe student participation and engagement...'}),
            'challenges_faced': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Describe any challenges or problems encountered...'}),
            'solutions_implemented': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Describe solutions or strategies implemented...'}),
            'next_lesson_plan': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Describe your plan for the next lesson/period...'}),
            'additional_notes': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Any additional notes or observations...'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    'class': 'w-full px-3 lg:px-4 py-2.5 lg:py-3 rounded-xl text-sm border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-300'
                })
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs.update({
                    'class': 'w-full px-3 lg:px-4 py-2.5 lg:py-3 rounded-xl text-sm border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-300'
                })
            else:
                field.widget.attrs.update({
                    'class': 'w-full px-3 lg:px-4 py-2.5 lg:py-3 rounded-xl text-sm border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-300'
                })

class TeacherWorkplanForm(forms.ModelForm):
    class Meta:
        model = TeacherWorkplan
        fields = [
            'subject', 'class_obj', 'plan_type', 'academic_year', 'term',
            'learning_objectives', 'topics_to_cover', 'teaching_methods', 
            'assessment_methods', 'resources_needed', 'timeline',
            'achievements', 'challenges_encountered', 'solutions_applied', 
            'student_performance_analysis', 'recommendations'
        ]
        widgets = {
            'learning_objectives': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Describe the learning objectives for the term...'}),
            'topics_to_cover': forms.Textarea(attrs={'rows': 4, 'placeholder': 'List the topics to be covered during the term...'}),
            'teaching_methods': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Describe teaching methods and strategies to be used...'}),
            'assessment_methods': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Describe assessment methods and evaluation criteria...'}),
            'resources_needed': forms.Textarea(attrs={'rows': 3, 'placeholder': 'List resources and materials needed...'}),
            'timeline': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Describe timeline and schedule for topics...'}),
            'achievements': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Describe achievements and successes (for end of term)...'}),
            'challenges_encountered': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Describe challenges and problems encountered (for end of term)...'}),
            'solutions_applied': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Describe solutions and strategies applied (for end of term)...'}),
            'student_performance_analysis': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Analyze student performance (for end of term)...'}),
            'recommendations': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Provide recommendations for improvement (for end of term)...'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    'class': 'w-full px-3 lg:px-4 py-2.5 lg:py-3 rounded-xl text-sm border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-300'
                })
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs.update({
                    'class': 'w-full px-3 lg:px-4 py-2.5 lg:py-3 rounded-xl text-sm border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-300'
                })
            else:
                field.widget.attrs.update({
                    'class': 'w-full px-3 lg:px-4 py-2.5 lg:py-3 rounded-xl text-sm border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-300'
                })

class LogbookReviewForm(forms.ModelForm):
    class Meta:
        model = TeacherLogbook
        fields = ['status', 'review_comments']
        widgets = {
            'review_comments': forms.Textarea(attrs={
                'rows': 4, 
                'placeholder': 'Provide feedback and comments for the teacher...',
                'class': 'w-full px-3 lg:px-4 py-2.5 lg:py-3 rounded-xl text-sm border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-300'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].widget.attrs.update({
            'class': 'w-full px-3 lg:px-4 py-2.5 lg:py-3 rounded-xl text-sm border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-300'
        })

class WorkplanReviewForm(forms.ModelForm):
    class Meta:
        model = TeacherWorkplan
        fields = ['status', 'review_comments']
        widgets = {
            'review_comments': forms.Textarea(attrs={
                'rows': 4, 
                'placeholder': 'Provide feedback and comments for the teacher...',
                'class': 'w-full px-3 lg:px-4 py-2.5 lg:py-3 rounded-xl text-sm border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-300'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].widget.attrs.update({
            'class': 'w-full px-3 lg:px-4 py-2.5 lg:py-3 rounded-xl text-sm border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-300'
        })
