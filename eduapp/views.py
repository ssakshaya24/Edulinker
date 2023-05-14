
from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from .models import *

from django.db.models import Count



# from rest_framework.response import Response
# from rest_framework.views import APIView
# from eduapp.serializers import MySerializer
# from django.views.decorators.csrf import csrf_exempt


# Create your views here.



def home(request):
    return render(request,'home.html')

def parentlogin(request):
    if(request.method=="POST"):
        rollNumber = request.POST["roll"]
        password = request.POST["password"]
        pcheck = Parents.objects.get(rollno=rollNumber)

        if(password==pcheck.password):
            request.session['parentID']=pcheck.pid
            return redirect("parenthome")
        else:
            return HttpResponse("Invalid Username or Password!")
    else:
        return render(request,'parentlogin.html')
    
def parenthome(request):
    pid = request.session['parentID']
    parentdetail = Parents.objects.get(pid=pid)
    pname=parentdetail.parentname



    return render(request,"parenthome.html",locals())

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
        teachert=Teacher.objects.get(Class=standard)
        parentt=Parents.objects.last()
        TeacherParent.objects.create(pid=parentt,tid=teachert)
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
            request.session['TeacherId']=tcheck.tid
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
    tid=request.session['TeacherId']
    tchoose=Teacher.objects.get(tid=tid)
    tname=tchoose.teacherName
    print(tname)
    return render(request,'teacherhome.html',locals())

def updateAttendance(request):
    if(request.method=="POST"):
        absentdate = request.POST['date']
        absentrollno = request.POST['rollno']

        ar = Parents.objects.get(rollno=absentrollno)
        Absentees.objects.create(absentDate=absentdate,rollNo=ar)
        print("successful")
        return redirect("updateattendance")
    else:
         return render(request,'updateattendance.html')
        

def viewattendance(request):
    pid = request.session.get('parentID')

    student=Parents.objects.get(pid=pid)
    sname=student.studentname
    sroll=student.rollno
    count = Absentees.objects.filter(rollNo=pid).count()
    presentday=120-count
    percentage=round((presentday/120)*100,2)



    return render(request,'view_attendance.html',locals())

def aboutus(request):
    return render(request,'aboutus.html')
   
def updatetestresult(request):
    if(request.method=="POST"):
        tdate=request.POST['tdate']
        Rollno=request.POST['rollno']
        subject=request.POST['subject']
        topic=request.POST['topic']
        total=request.POST['total']
        mark=request.POST['mark']
        ptuple=Parents.objects.get(rollno=Rollno)

        TestResults.objects.create(rollNo=ptuple,tDate=tdate,subject=subject,topic=topic,total=total,score=mark)
        return HttpResponse("Test Record Created")

    return render(request,'updatetestresult.html')


def viewtestresults(request):
    pid=request.session['parentID']
    # print(pid)
    ptuple=Parents.objects.get(pid=pid)
    sroll=ptuple.pid
    sname=ptuple.studentname
    Testdetails=TestResults.objects.filter(rollNo=sroll)
    # print(Testdetails)
    d={"t":Testdetails,"roll":sroll,"name":sname}
    return render(request,"viewtestresults.html",d)


def message(request):
    if(request.method=="POST"):
        msg = request.POST['msg']

        pid =request.session['parentID']
        
        pt = Parents.objects.get(pid=pid)
        tp = TeacherParent.objects.get(pid=pid)
        t = tp.tid.tid
        print(t)
        teach = Teacher.objects.get(tid=t)

        print("Parent ID : " , pt.pid)
        print("Teacher ID : " , teach.tid)
        Message.objects.create(sender=pt,receiver=teach,content=msg)
        print(msg)

        return HttpResponse("Success")
       

        #prntuple = TeacherParent.objects.get(pid=pid)
    pid =request.session['parentID']
    mtuple=Message.objects.filter(sender=pid)   
    print(mtuple)
    d={"mesg":mtuple}

    return render(request,'message.html',d)
    
""" class MyView(APIView):
    def get(self, request):
        data = {
            'field1': 'Hello',
            'field2': 42,
        }
        serializer = MySerializer(data)
        return Response(serializer.data)
 """
