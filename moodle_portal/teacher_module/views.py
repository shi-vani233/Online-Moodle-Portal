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
from student_module.models import StudentCourse,Submission
import datetime
from django.core import paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def teacher_home(request):
    if request.user.is_authenticated:
        loggedin_user=request.user.username
        t=Teacher.objects.get(teacher_email=loggedin_user)
        courses=Course.objects.filter(teacher=t)
        assignment=Assignment.objects.filter(teacher=t)
        if assignment.exists():
            paginator = Paginator(assignment,5)
            page = request.GET.get('page', 1)
            try:
                assignment = paginator.page(page)
            except PageNotAnInteger:
                users = paginator.page(1)
            except EmptyPage:
                users = paginator.page(paginator.num_pages)
            return render(request, 'teacher_home.html',{'user':t,'assignment':assignment,'courses':courses})
        return render(request,'teacher_home.html',{'user':t,'assignment':assignment,'courses':courses})

def teacher_courses(request):
    if request.user.is_authenticated:
        loggedin_user=request.user.username
        t=Teacher.objects.get(teacher_email=loggedin_user)
        courses=Course.objects.filter(teacher=t)
        return render(request,'teacher_courses.html',{'user':t,'courses':courses})

def add_course(request):
    if request.user.is_authenticated:
        loggedin_user=request.user.username
        course_id=request.POST.get('course_id','')
        course_id=course_id.upper()
        course_name=request.POST.get('course_name','')
        course_branch=request.POST.get('course_branch','')
        print(course_id)
        t=Teacher.objects.get(teacher_email=loggedin_user)
        courses=Course.objects.filter(teacher=t)
        c=Course.objects.all()
        for i in c:
            if i.course_id==course_id:
                msg="this ID is given"
                return render(request ,'teacher_courses.html',{'user':t,'courses':courses,'msg':msg})
        c=Course(course_id=course_id,course_name=course_name,course_branch=course_branch,teacher=t)
        c.save()
        return render(request ,'teacher_courses.html',{'user':t,'courses':courses})

def add_assignment(request):
    if request.user.is_authenticated:
        loggedin_user=request.user.username
        assignment_title=request.POST.get('assignment_title','')
        course_id=request.POST.get('course','')
        due_date=request.POST.get('due_date','')
        assignment_file=request.FILES['assignment_file']
        added_date=datetime.datetime.now() 
        course=Course.objects.get(course_id=course_id)
        teacher=Teacher.objects.get(teacher_email=loggedin_user)
        a=Assignment(assignment_title=assignment_title,due_date=due_date,assignment_file=assignment_file,added_date=added_date,course=course,teacher=teacher)
        a.save()
        assignment=Assignment.objects.filter(teacher=teacher)
        courses=Course.objects.filter(teacher=teacher)
        if assignment.exists():
            paginator = Paginator(assignment,5)
            page = request.GET.get('page', 1)
            try:
                assignment = paginator.page(page)
            except PageNotAnInteger:
                users = paginator.page(1)
            except EmptyPage:
                users = paginator.page(paginator.num_pages)
            return render(request, 'teacher_home.html',{'user':teacher,'assignment':assignment,'courses':courses})
        return render(request,'teacher_home.html',{'user':teacher,'assignment':assignment,'courses':courses})


def view_all_submission(request):
    if request.user.is_authenticated:
        loggedin_user=request.user.username
        t=Teacher.objects.get(teacher_email=loggedin_user)
        ass_id=request.GET.get('a_id','')
        assignment=Assignment.objects.get(assignment_id=ass_id)
        submissions=Submission.objects.filter(assignment=assignment)
        return render(request,'view_all_submission.html',{'submissions':submissions,'ass_id':ass_id,'user':t,'assignment':assignment})

def give_marks(request):
    if request.user.is_authenticated:
        loggedin_user=request.user.username
        t=Teacher.objects.get(teacher_email=loggedin_user)
        sub_id=request.POST.get('s_id','')
        marks=request.POST.get('marks','')
        sub=Submission.objects.get(submission_id=sub_id)
        sub.marks=marks
        sub.save()
        ass_id=request.POST.get('a_id','')
        assignment=Assignment.objects.get(assignment_id=ass_id)
        submissions=Submission.objects.filter(assignment=assignment)
        return render(request,'view_all_submission.html',{'submissions':submissions,'ass_id':ass_id,'user':t})
       
def delete_assignment(request):
    if request.user.is_authenticated:
        loggedin_user=request.user.username
        t=Teacher.objects.get(teacher_email=loggedin_user)
        ass_id=request.GET.get('a_id','')
        a1=Assignment.objects.get(assignment_id=ass_id)
        a1.delete()
        courses=Course.objects.filter(teacher=t)
        assignment=Assignment.objects.filter(teacher=t)
        msg="Assignment deleted successfully!"
        if assignment.exists():
            paginator = Paginator(assignment,5)
            page = request.GET.get('page', 1)
            try:
                assignment = paginator.page(page)
            except PageNotAnInteger:
                users = paginator.page(1)
            except EmptyPage:
                users = paginator.page(paginator.num_pages)
            return render(request, 'teacher_home.html',{'user':t,'assignment':assignment,'courses':courses,'msg':msg})
        return render(request,'teacher_home.html',{'user':t,'assignment':assignment,'courses':courses,'msg':msg})

def view_students(request):
    if request.user.is_authenticated:
        loggedin_user=request.user.username
        t=Teacher.objects.get(teacher_email=loggedin_user)
        c_id=request.GET.get('c_id','')
        course=Course.objects.get(course_id=c_id)
        stu_course=StudentCourse.objects.filter(course=course)
        return render(request,'view_students.html',{'stu_course':stu_course,'course':course})

def logout(request):
    auth.logout(request)
    return redirect('/')