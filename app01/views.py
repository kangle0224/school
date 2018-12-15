from django.shortcuts import render, HttpResponse
from app01 import models

def students(request):
    class_list = models.Classes.objects.all()
    stu_list = models.Student.objects.all()
    return render(request, 'students.html', {"stu_list": stu_list,"class_list":class_list})

def add_student(request):
    response = {"status": True, 'msg': None,'data':None}
    try:
        u = request.POST.get('user')
        a = request.POST.get('age')
        g = request.POST.get('gender')
        c = request.POST.get('cls_id')
        obj = models.Student.objects.create(
            username=u,
            age=a,
            gender=g,
            cs_id=c
        )
        response["data"] = obj.id

    except Exception as e:
        response["status"] = False
        response["msg"] = '用户输入错误'
        print(e)
        print(response)
    import json
    return HttpResponse(json.dumps(response, ensure_ascii=False))
