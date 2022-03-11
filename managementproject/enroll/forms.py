from django import forms
from django.core import validators
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'
        widgets={
        'name':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.TextInput(attrs={'class':'form-control'}),
        'password':forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),
        }
