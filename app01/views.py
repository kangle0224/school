from django.shortcuts import render
from app01 import models

def students(request):
    class_list = models.Classes.objects.all()
    stu_list = models.Student.objects.all()
    return render(request, 'students.html', {"stu_list": stu_list,"class_list":class_list})