from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser

class Municipality(models.Model):
    municipality_name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.municipality_name

class Brgy(models.Model):
    brgy_name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    # image = models.ImageField(upload_to='item_images', blank=True, null=True)
    
    def __str__(self):
        return self.brgy_name
    
class School(models.Model):
    school_name = models.CharField(max_length=150)
    address = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=15, choices=[
        ('Public', 'Public'), ('Private', 'Private')
    ])
    
    def __str__(self):
        return self.school_name
    
class Course(models.Model):
    course_name = models.CharField(max_length=150)
    # image = models.ImageField(upload_to='item_images', blank=True, null=True)
    
    def __str__(self):
        return self.school_name
    
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=[
        ('Male', 'Male'), ('Female', 'Female')
    ])
    birth_date = models.DateField()
    contact_no = models.CharField(max_length=10)
    address = models.TextField()
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE)
    brgy = models.ForeignKey(Brgy, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=[
        ('Current', 'Current'), ('Graduated', 'Graduated')
    ])

    def __str__(self):
        return self.first_name + " " + self.last_name