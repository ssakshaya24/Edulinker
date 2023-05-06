# Generated by Django 4.1.3 on 2023-05-06 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eduapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('tid', models.AutoField(primary_key=True, serialize=False)),
                ('teacherName', models.CharField(max_length=25)),
                ('Class', models.CharField(max_length=2)),
                ('section', models.CharField(max_length=1)),
                ('password', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherParent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eduapp.parents')),
                ('tid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eduapp.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('absentDate', models.DateField()),
                ('Class', models.CharField(max_length=2)),
                ('section', models.CharField(max_length=1)),
                ('rollNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eduapp.parents')),
            ],
        ),
        migrations.CreateModel(
            name='ApplyLeave',
            fields=[
                ('lid', models.AutoField(primary_key=True, serialize=False)),
                ('fromDate', models.DateField()),
                ('toDate', models.DateField()),
                ('reason', models.TextField()),
                ('rollNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eduapp.parents')),
            ],
        ),
    ]