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

# Create your views here.
def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def teacher_register(request):
    return render(request,'teacher_register.html',context=None)

def student_register(request):
    return render(request,'student_register.html',context=None)

def add_teacher(request):
    teacher_name=request.POST.get('teacher_name','')
    teacher_email=request.POST.get('teacher_email','') 
    teacher_password=request.POST.get('teacher_password','')
    teacher_dob=request.POST.get('teacher_dob','')
    teacher_gender=request.POST.get('teacher_gender','')  
    teacher_address=request.POST.get('teacher_address','')
    teacher_city=request.POST.get('teacher_city','')
    teacher_state=request.POST.get('teacher_state','')
    teacher_mobile_no=request.POST.get('teacher_mobile_no','')   
    
    if len(teacher_password)<6:
        msg_pass="password and confirm password must be same with minimum length 6"
    else:
        msg_pass=''
    if len(teacher_mobile_no)!=10:
        msg_phone="phone number must be of length 10"
    else:
        msg_phone=''
    if not (msg_pass or msg_phone):
        try:
            user=User.objects.create_user(username=teacher_email,email=teacher_email,password=teacher_password)
            user.save()
            tea=Teacher(teacher_name=teacher_name,teacher_email=teacher_email,teacher_dob=teacher_dob,
                teacher_gender=teacher_gender,teacher_address=teacher_address,teacher_city=teacher_city,teacher_state=teacher_state,teacher_mobile_no=teacher_mobile_no)
            tea.save()
            msg="you are successfully registered, Go for Login!"
            return render(request ,'login.html',{'msg':msg})
        except:
            msg_error="this email is already registered"
            return render(request,'teacher_register.html',{'msg_error':msg_error})
    else:
        return render(request ,'teacher_register.html',{'msg_pass':msg_pass,'msg_phone':msg_phone})


def add_student(request):
    student_name=request.POST.get('student_name','')
    student_email=request.POST.get('student_email','') 
    student_password=request.POST.get('student_password','')
    student_dob=request.POST.get('student_dob','')
    student_gender=request.POST.get('student_gender','')  
    student_semester=request.POST.get('student_semester','')  
    student_branch=request.POST.get('student_branch','')  
    student_address=request.POST.get('student_address','')
    student_city=request.POST.get('student_city','')
    student_state=request.POST.get('student_state','')
    student_mobile_no=request.POST.get('student_mobile_no','')   
    if len(student_password)<6:
        msg_pass="password and confirm password must be same with minimum length 6"
    else:
        msg_pass=''
    if len(student_mobile_no)!=10:
        msg_phone="phone number must be of length 10"
    else:
        msg_phone=''
    if not (msg_pass or msg_phone):
        try:
            user=User.objects.create_user(username=student_email,email=student_email,password=student_password)
            user.save()
            stu=Student(student_name=student_name,student_email=student_email,student_dob=student_dob,
                student_gender=student_gender,student_semester=student_semester,student_branch=student_branch,
                student_address=student_address,student_city=student_city,student_state=student_state,student_mobile_no=student_mobile_no)
            stu.save()
            if(request.FILES.get('student_image','')):
                student_image=request.FILES['student_image']
                s=Student.objects.get(student_email=student_email)
                s.student_image=student_image
                s.save()
            msg="you are successfully registered, Go for Login!"
            return render(request ,'login.html',{'msg':msg})
        except:
            msg_error="this email is already registered"
            return render(request,'student_register.html',{'msg_error':msg_error})
    else:
        return render(request ,'student_register.html',{'msg_pass':msg_pass,'msg_phone':msg_phone})

def authenticate(request):
    email=request.POST.get('email','')
    password=request.POST.get('password','')
    User=auth.authenticate(username=email,password=password)
    if User is not None:
        auth.login(request,User)
        stu=Student.objects.filter(student_email=email)
        tea=Teacher.objects.filter(teacher_email=email)
        if stu.exists():
            return HttpResponseRedirect('/student_module/student_home')
        if tea.exists():
            return HttpResponseRedirect('/teacher_module/teacher_home')
    else:
        msg = "Invalid Username or Password!"
        return render(request,'login.html',{'msg_login':msg})


    