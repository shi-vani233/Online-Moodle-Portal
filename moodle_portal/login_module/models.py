from django.db import models

# Create your models here.
class Teacher(models.Model):
    teacher_email=models.CharField(max_length=20,primary_key=True,help_text ='write your email')
    teacher_name=models.CharField(max_length=20)
    teacher_gender=models.CharField(max_length=10)
    teacher_dob=models.DateTimeField()
    teacher_address=models.CharField(max_length=100,help_text = 'write your address')
    teacher_city=models.CharField(max_length=20)
    teacher_state=models.CharField(max_length=20)
    teacher_mobile_no=models.CharField(max_length=10)
    def __str__(self):
        return self.teacher_name

class Student(models.Model):
    student_email=models.CharField(max_length=20,primary_key=True,help_text ='write your email')
    student_name=models.CharField(max_length=20)
    student_gender=models.CharField(max_length=10)
    student_semester=models.IntegerField()
    student_branch=models.CharField(max_length=50)
    student_dob=models.DateTimeField()
    student_address=models.CharField(max_length=100,help_text = 'write your address')
    student_city=models.CharField(max_length=20)
    student_state=models.CharField(max_length=20)
    student_mobile_no=models.CharField(max_length=10)
    student_image=models.ImageField(upload_to='images/',blank=True)
    def __str__(self):
        return self.student_name