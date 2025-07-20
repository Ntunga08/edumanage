from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

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
