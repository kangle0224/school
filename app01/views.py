from django.shortcuts import render, HttpResponse
from app01 import models
import json

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

    return HttpResponse(json.dumps(response, ensure_ascii=False))

def del_student(request):
    ret = {"status": True}
    try:
        nid = request.GET.get("nid")
        v=models.Student.objects.filter(id=nid).delete()
        print(v)
    except Exception as e:
        ret["status"] = False

    return HttpResponse(json.dumps(ret))


def edit_student(request):
    response = {'code':1000,'msg': None}
    try:
        nid = request.POST.get('nid')
        user = request.POST.get('user')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        cls_id = request.POST.get('cls_id')
        models.Student.objects.filter(id=nid).update(
            username=user,
            age=age,
            gender=gender,
            cs_id=cls_id
        )
    except Exception as e:
        response["code"] = 1001
        response["msg"] = str(e)
    return HttpResponse(json.dumps(response))

def test(request):
    print(request.POST.getlist(""))
    return HttpResponse('....')