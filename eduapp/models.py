from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE, SET_DEFAULT
from django.utils import timezone

# Create your models here.


class Parents(models.Model):
    pid = models.AutoField(db_column='PID', primary_key=True)  # Field name made lowercase.
    parentname = models.CharField(db_column='ParentName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    rollno = models.CharField(db_column='RollNo', max_length=15, blank=True, null=True)  # Field name made lowercase.
    studentname = models.CharField(db_column='StudentName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    phonenum = models.BigIntegerField(db_column='PhoneNum', blank=True, null=True)  # Field name made lowercase.
    standard = models.CharField(db_column='Standard', max_length=3, blank=True, null=True)  # Field name made lowercase.
    section = models.CharField(db_column='Section', max_length=2, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=50, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'parents'
# class profile(models.Model):
#     username = models.ForeignKey(NewUser,on_delete=CASCADE)
#     workplace = models.CharField(max_length=30,null=True,blank=True)
#     phone = models.CharField(max_length=13,null=True)
#     gender = models.CharField(max_length=10,null=False,default='Male')
#     dob = models.DateField(blank=True,default='2001-08-08')
#     address_line_1 = models.CharField(max_length=50,null=True)
#     address_line_2 = models.CharField(max_length=50,null=True)
#     pin = models.IntegerField()
#     skill1 = models.CharField(max_length=50,blank=True)
#     skill2 = models.CharField(max_length=50,blank=True)
#     is_student = models.BooleanField(default=True)

class Teacher(models.Model):
    tid=models.CharField(primary_key=True,max_length=3)
    teacherName=models.CharField(null=False,max_length=25)
    Class=models.CharField(max_length=2,null=False)
    section=models.CharField(max_length=1,null=False)
    password=models.CharField(null=False,max_length=25)

class Attendance(models.Model):
    rollNo = models.ForeignKey(Parents,on_delete=CASCADE)
    absentDate = models.DateField(null=False)
    Class=models.CharField(max_length=2,null=False)
    section=models.CharField(max_length=1,null=False)

class TeacherParent(models.Model):
    tid=models.ForeignKey(Teacher,on_delete=CASCADE)
    pid=models.ForeignKey(Parents,on_delete=CASCADE)

class ApplyLeave(models.Model):
    
    lid=models.AutoField(primary_key=True)
    rollNo = models.ForeignKey(Parents,on_delete=CASCADE)
    fromDate=models.DateField(null=False)
    toDate=models.DateField(null=False)
    reason = models.TextField()



