from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('teacher_home/',views.teacher_home,name='teacher_home'),
    path('teacher_courses/',views.teacher_courses,name='teacher_coursese'),
    path('add_course/',views.add_course,name='add_course'),
    path('add_assignment/',views.add_assignment,name='add_assignment'),
    path('view_all_submission/',views.view_all_submission,name='view_all_submission'),
    path('give_marks/',views.give_marks,name='give_marks'),
    path('delete_assignment/',views.delete_assignment,name='delete_assignment'),
    path('view_students/',views.view_students,name='view_students'),
    path('logout/',views.logout,name='logout'),
]