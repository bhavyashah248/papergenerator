from django.contrib.auth.models import User
from . models import Teacher
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Teacher
        fields = ['name', 'subject', 'password']