from django.urls import path
from .views import *
# Base URL --> http://127.0.0.1:8000/emsapp

urlpatterns = [
    path('', home ),
    path('employee_record/', employee_record ),

]