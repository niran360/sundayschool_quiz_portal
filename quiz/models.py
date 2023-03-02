from django.db import models
from datetime import datetime
from django import forms

from student.models import Student
class Course(models.Model):
   course_name = models.CharField(max_length=50)
   question_number = models.PositiveIntegerField()
   total_marks = models.PositiveIntegerField()
   start_time = models.DateTimeField(default=datetime.now())
   end_time = models.DateTimeField(default=datetime.now())
   def __str__(self):
        return self.course_name

class Question(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    marks=models.PositiveIntegerField()
    question=models.CharField(max_length=600)
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200)
    option4=models.CharField(max_length=200)
    cat=(('Option1','Option1'),('Option2','Option2'),('Option3','Option3'),('Option4','Option4'))
    answer=models.CharField(max_length=200,choices=cat)

class Result(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    exam = models.ForeignKey(Course,on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)


# class Meta:
#         model = Course
#         fields = '__all__'
#         exclude = ['teacher']
#         widgets = {
#             'name': forms.TextInput(attrs = {'class':'form-control'}),
#             'total_marks' : forms.NumberInput(attrs = {'class':'form-control'}),
#             'start_time': forms.DateTimeInput(attrs = {'class':'form-control'}),
#             'end_time': forms.DateTimeInput(attrs = {'class':'form-control'})
#         }

