from django.shortcuts import render
from django.http import JsonResponse

from .models import Classroom, Student
from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView
from .serializers import Studentserializer, Classroomserializer


class student_list(ListAPIView):
	queryset = Student.objects.all()
	serializer_class = Studentserializer
		
class classroom_list(ListAPIView):
	queryset = Classroom.objects.all()
	serializer_class = Classroomserializer

class teacher_classes(ListAPIView):

    queryset = Classroom.objects.all()
    serializer_class = Classroomserializer

    def get_queryset(self):
        return User.objects.get(id = self.kwargs['teacher_id']).instructor.all()
        #return Classroom.objects.filter(teacher = self.kwargs['teacher_id'])

class students_inclass(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = Studentserializer

    def get_queryset(self):
        return Classroom.objects.get(id = self.kwargs['class_id']).related.all()


# Create your views here.
