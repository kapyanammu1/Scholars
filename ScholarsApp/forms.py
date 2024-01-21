from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User, Permission
from .models import Municipality, Brgy, School, Course, Student
from django.core.exceptions import ValidationError

class MunicipalityForm(forms.ModelForm):
    class Meta:
        model = Municipality
        fields = ('municipality_name', 'description',)
        widgets = {
            'municipality_name': forms.TextInput(attrs={
            'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
            'class': 'form-control',
            }),
        }

class BrgyForm(forms.ModelForm):
    class Meta:
        model = Brgy
        fields = ('brgy_name', 'description',)
        widgets = {
            'brgy_name': forms.TextInput(attrs={
            'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
            'class': 'form-control',
            }),
        }

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ('school_name', 'address', 'type',)
        widgets = {
            'school_name': forms.TextInput(attrs={
            'class': 'form-control',
            }),
            'address': forms.TextInput(attrs={
            'class': 'form-control',
            }),
            'type': forms.Select(attrs={
            'class': 'form-select',
            }),
        }

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('course_name',)
        widgets = {
            'course_name': forms.TextInput(attrs={
            'class': 'form-control',
            }),
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('first_name','middle_name','last_name','gender','birth_date','contact_no','address','municipality','brgy','school','course','status',)
        widgets = {
            'first_name': forms.TextInput(attrs={
            'class': 'form-control',
            }),
            'middle_name': forms.TextInput(attrs={
            'class': 'form-control',
            }),
            'last_name': forms.TextInput(attrs={
            'class': 'form-control',
            }),
            'gender': forms.Select(attrs={
            'class': 'form-select',
            }),
            'birth_date': forms.DateInput(attrs={
            'class': 'form-control',
            }),
            'contact_no': forms.TextInput(attrs={
            'class': 'form-control',
            }),
            'address': forms.TextInput(attrs={
            'class': 'form-control',
            }),
            'municipality': forms.Select(attrs={
            'class': 'form-select',
            }),
            'brgy': forms.Select(attrs={
            'class': 'form-select',
            }),
            'school': forms.Select(attrs={
            'class': 'form-select',
            }),
            'course': forms.Select(attrs={
            'class': 'form-select',
            }),
            'status': forms.Select(attrs={
            'class': 'form-select',
            }),
        }