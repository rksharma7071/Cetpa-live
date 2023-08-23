from django.contrib import admin
from .models import *


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','name','age', 'city','mobileno','salary']