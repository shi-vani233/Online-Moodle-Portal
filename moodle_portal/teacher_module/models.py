from django.db import models
from login_module.models import Teacher

# Create your models here.
class Course(models.Model):
    course_id=models.CharField(max_length=10,primary_key=True)
    course_name=models.CharField(max_length=50)
    course_branch=models.CharField(max_length=20)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE,default=None,related_name="course_teacher")
    def __str__(self):
        return str(self.course_id) + ": " + str(self.course_name)

class Assignment(models.Model):
    assignment_id=models.AutoField(primary_key=True)
    assignment_title=models.CharField(max_length=50)
    assignment_file=models.FileField(upload_to='assignments/',null=True)
    added_date=models.DateTimeField()
    due_date=models.DateTimeField()
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE,default=None,related_name="assignment_teacher")
    course=models.ForeignKey(Course,on_delete=models.CASCADE,default=None,related_name="assignment_course")
    def __str__(self):
        return  str(self.assignment_title)  + ":::: " + str(self.course)