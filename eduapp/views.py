from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from eduapp.serializers import MySerializer
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def updateAttendance(request):
    return render(request,'updateattendance.html')

def home(request):
    return render(request,'home.html')

def parentlogin(request):
    return render(request,'parentlogin.html')

def parentreg(request):
    return render(request,'parentreg.html')

    
class MyView(APIView):
    def get(self, request):
        data = {
            'field1': 'Hello',
            'field2': 42,
        }
        serializer = MySerializer(data)
        return Response(serializer.data)
