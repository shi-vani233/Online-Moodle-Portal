import cgi,os,sys
import cgitb
from django.db.models.fields import DateTimeField, EmailField
from django.http.response import HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.core.mail import send_mail
from login_module.models import Student,Teacher
from teacher_module.models import Course,Assignment
from .models import StudentCourse,Submission
from django.views.decorators.clickjacking import xframe_options_exempt
import datetime

# Create your views here.

def student_home(request):
    if request.user.is_authenticated:
        loggedin_user=request.user.username
        s=Student.objects.get(student_email=loggedin_user)
        sc=StudentCourse.objects.filter(student=s)
        courses=[]
        for i in sc:
            courses.append(i.course)
            print(i.course)
        assignments=[]
        for i in courses:
            a=Assignment.objects.filter(course=i)
            for j in a:
                print(j.assignment_title,j.course)
                assignments.append(j)
        pending_assignment=[]
        for i in assignments:
            print(i)
            sub=Submission.objects.filter(student=s,assignment=i)
            if sub.exists():
                for j in sub:
                    print("submitted",j)
            else:
                pending_assignment.append(i)
        for i in pending_assignment:
            print("p  :",i.assignment_title)
        now_date=datetime.datetime.now()
        print(now_date)
        return render(request,'student_home.html',{'assignments':pending_assignment,'user':s,'now_date':now_date})

def student_courses(request):
    if request.user.is_authenticated:
        loggedin_user=request.user.username
        student=Student.objects.get(student_email=loggedin_user)
        student_branch=student.student_branch
        courses=Course.objects.filter(course_branch=student_branch)
        sc=StudentCourse.objects.filter(student=student)
        unenrolled_courses=[]
        enrolled_courses=[]
        for i in courses:
            for j in sc:
                if i.course_id==j.course.course_id:
                    enrolled_courses.append(i)
        for i in courses:
            if i not in enrolled_courses:
                unenrolled_courses.append(i)
        
        return render(request,'student_courses.html',{'enrolled_courses':enrolled_courses,'unenrolled_courses':unenrolled_courses,'user':student})

def enroll_course(request):
    if request.user.is_authenticated:
        loggedin_user=request.user.username
        student=Student.objects.get(student_email=loggedin_user)
        course_id=request.GET.get('c_id','')
        course=Course.objects.get(course_id=course_id)
        new_course=StudentCourse(student=student,course=course)
        new_course.save()
        return student_courses(request)

def leave_course(request):
    if request.user.is_authenticated:
        loggedin_user=request.user.username
        student=Student.objects.get(student_email=loggedin_user)
        course_id=request.GET.get('c_id','')
        course=Course.objects.get(course_id=course_id)
        del_course=StudentCourse.objects.get(student=student,course=course)
        del_course.delete()
        return student_courses(request)

def upload_submission(request):
    if request.user.is_authenticated:
        loggedin_user=request.user.username
        student=Student.objects.get(student_email=loggedin_user)
        ass_id=request.POST.get('a_id','')
        assignment=Assignment.objects.get(assignment_id=ass_id)
        submission_file=request.FILES['submission_file']
        submission_added_date=datetime.datetime.now()
        s=Submission(submission_file=submission_file,submission_added_date=submission_added_date,assignment=assignment,student=student)
        s.save()
        msg="Submission uploaded sucessfully!"
        sc=StudentCourse.objects.filter(student=student)
        courses=[]
        for i in sc:
            courses.append(i.course)
            print(i.course)
        assignments=[]
        for i in courses:
            a=Assignment.objects.filter(course=i)
            for j in a:
                print(j.assignment_title,j.course)
                assignments.append(j)
        pending_assignment=[]
        for i in assignments:
            print(i)
            sub=Submission.objects.filter(student=student,assignment=i)
            if sub.exists():
                for j in sub:
                    print("submitted",j)
            else:
                pending_assignment.append(i)
        for i in pending_assignment:
            print("p  :",i.assignment_title)
        return render(request,'student_home.html',{'assignments':pending_assignment,'msg':msg,'user':student})
        

def view_assignment(request):
    if request.user.is_authenticated:
        loggedin_user=request.user.username
        student=Student.objects.get(student_email=loggedin_user)
        ass_id=request.GET.get('a_id','')
        assignment=Assignment.objects.get(assignment_id=ass_id)
        print(assignment)
        return render(request,'view_assignment.html',{'assignment':assignment,'user':student})

def student_assignments(request):
    if request.user.is_authenticated:
        loggedin_user=request.user.username
        student=Student.objects.get(student_email=loggedin_user)
        sub=Submission.objects.filter(student=student).order_by('-submission_added_date')
        for i in sub:
            print(i.assignment.course,"----",i.assignment)
        return render(request,'student_assignments.html',{'sub':sub,'user':student})

def logout(request):
    auth.logout(request)
    return redirect('/')
