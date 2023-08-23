from django.urls import path
from .views import *


urlpatterns = [

    path('register', view_register, name='register'),
    path('login', view_login, name='login'),
    path('', all_student, name='all_student'),
    path('student_payment/', student_payment, name="student_payment"),
    path('student_reg/', student_reg, name="student_reg"),
    path('all_courses/', all_courses, name='all_courses'),
    path('course_student/', course_student, name="course_student"),
    path('course_reg/', course_reg, name='course_reg'),
    path('all_payment/', all_payment, name='all_payment'),
    path('PaymentDetails_reg/', PaymentDetails_reg, name='PaymentDetails_reg'),
    path('showstu/<int:id>/', view_show_student, name='showstu'),
]
