from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('teacher_register/',views.teacher_register,name='teacher_register'),
    path('student_register/',views.student_register,name='student_register'),
    path('add_student/',views.add_student,name='add_student'),
    path('add_teacher/',views.add_teacher,name='add_teacher'),
    path('authenticate/',views.authenticate,name='authenticate'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)