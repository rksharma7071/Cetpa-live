from django.contrib import admin
from .models import *


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'mobileno','dob','pic','create_date','last_update']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name']
