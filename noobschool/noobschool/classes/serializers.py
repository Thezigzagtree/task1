from .models import Student, Classroom
from rest_framework import serializers

class Classroomserializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['name', 'subject', 'year', 'teacher']
        
class Studentserializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'date_of_birth', 'gender', 'exam_grade', 'classroom', 'image']