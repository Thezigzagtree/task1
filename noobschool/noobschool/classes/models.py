from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers
from model_utils import Choices

class Classroom(models.Model):

    name = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    year = models.IntegerField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'instructor')

    def __str__(self):
        return self.name

class Student(models.Model):
    genderchoices = Choices(
        ("M","Male"),
        ("F","Female"),
    )
        
    name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length = 1, choices = genderchoices, default = genderchoices['M'])
    exam_grade = models.IntegerField()
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='related')
    image= models.ImageField(null = True, blank = True)

    def __str__(self):
        return self.name

# Create your models here.
