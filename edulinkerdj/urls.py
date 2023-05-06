"""edulinkerdj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from eduapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('parent_registration',views.parentreg,name="parentreg"),
    path('parent_login',views.parentlogin,name="parentlogin"),
    path('apply_leave',views.applyleave,name="applyleave"),
    path('parent_home',views.parenthome,name="parenthome"),
    path('teacher_login',views.teacherlogin,name="teacherlogin"),
    path('teacher_reg',views.teacherreg,name="teacherreg"),
    path('teacher_home',views.teacherhome,name="teacherhome"),
    path('update_attendance',views.updateAttendance,name="updateattendance"),
    path('view_attendance',views.viewattendance,name="viewattendance")



    #path('myview/', views.MyView.as_view())


]
