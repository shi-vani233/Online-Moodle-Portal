from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('student_home/',views.student_home,name='student_home'),
    path('student_courses/',views.student_courses,name='student_courses'),
    path('enroll_course/',views.enroll_course,name='enroll_course'),
    path('leave_course/',views.leave_course,name='leave_course'),
    path('view_assignment/',views.view_assignment,name='view_assignment'),
    path('upload_submission/',views.upload_submission,name='upload_submission'),
    path('student_assignments/',views.student_assignments,name='student_assignments'),
    path('logout/',views.logout,name='logout'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)