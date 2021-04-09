from django.db import models
from login_module.models import Student
from teacher_module.models import Course,Assignment

# Create your models here.


class StudentCourse(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE,default=None,related_name="student")
    course=models.ForeignKey(Course,on_delete=models.CASCADE,default=None,related_name="course")
    class Meta:
        unique_together = ('student', 'course')
    def __str__(self):
        return str(self.student) + ":" + str(self.course)

class Submission(models.Model):
    submission_id=models.AutoField(primary_key=True)
    submission_file=models.FileField(upload_to='submissions/',null=True)
    submission_added_date=models.DateTimeField(default=None)
    marks = models.FloatField(null=True, default=None)
    assignment=models.ForeignKey(Assignment,on_delete=models.CASCADE,default=None,related_name="assignment")
    student=models.ForeignKey(Student,on_delete=models.CASCADE,default=None,related_name="assignment_student")
    def __str__(self):
        return str(self.student) + ":" + str(self.assignment)
    
    