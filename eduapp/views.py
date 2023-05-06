





from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from .models import *

from rest_framework.response import Response
from rest_framework.views import APIView
from eduapp.serializers import MySerializer
from django.views.decorators.csrf import csrf_exempt


# Create your views here.



def home(request):
    return render(request,'home.html')

def parentlogin(request):
    if(request.method=="POST"):
        rollNumber = request.POST["roll"]
        password = request.POST["password"]

        pcheck = Parents.objects.get(rollno=rollNumber)
        if(password==pcheck.password):
            return redirect("parenthome")
        else:
            return HttpResponse("Invalid Username or Password!")
    else:
        return render(request,'parentlogin.html')
    
def parenthome(request):
    return render(request,"parenthome.html")

def parentreg(request):
    if(request.method=="POST"):
        parentName = request.POST["pname"]
        rollNo = request.POST["rollno"]
        studentName =request.POST["sname"]
        phoneNumber =request.POST["ph_num"]
        standard = request.POST["class"]
        address = request.POST["address"]
        password = request.POST["password"]
        section = request.POST["section"]
        Parents.objects.create(parentname=parentName,rollno=rollNo,studentname=studentName,phonenum=phoneNumber,standard=standard,section=section,address=address,password=password)
        return redirect('parentlogin')
    else:
        return render(request,'parentreg.html')
    

def applyleave(request):
    if(request.method=="POST"):
        parentid = request.POST["pid"]
        rollnumber = request.POST["roll_number"]

        leavecheck = Parents.objects.get(pid=parentid)
        if(leavecheck.rollno==rollnumber):
            return HttpResponse("Leave applied successfully!")
        else:
            return HttpResponse("Invalid credentials!")
    else:
         return render(request,'applyleave.html')

def teacherlogin(request):
    if(request.method=="POST"):
        teacherid = request.POST['yourid']
        password = request.POST['password']

        tcheck = Teacher.objects.get(tid=teacherid)
        if(password == tcheck.password):
            return redirect("teacherhome")
        else:
            return HttpResponse("Invalid username or password")
        return HttpResponse("Logged In")
    else:
        return render(request,'teacherlogin.html')

def teacherreg(request):
    if(request.method=="POST"):
        # teacherid = request.POST['tid']
        teachername = request.POST['tname']
        tclass = request.POST['standard']
        tsection = request.POST['section']
        tpassword = request.POST['password']
        
        Teacher.objects.create(teacherName=teachername,
        Class=tclass,section=tsection,password=tpassword)
        print("successful")
        return redirect("teacherlogin")
        
    else:
        return render(request,'teacherreg.html')

def teacherhome(request):
    return render(request,'teacherhome.html')

def updateAttendance(request):
    return render(request,'updateattendance.html')

    
""" class MyView(APIView):
    def get(self, request):
        data = {
            'field1': 'Hello',
            'field2': 42,
        }
        serializer = MySerializer(data)
        return Response(serializer.data)
 """