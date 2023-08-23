from django.shortcuts import render
from django.http import HttpResponse
from EMS.models import *


def home(request):
    if request.method == "GET":
        return render(request, 'EMS/home.html')
    elif request.method == "POST":
        if 'btnadd' in request.POST:
            emp = Employee()
            emp.name = request.POST.get('empname').lower()
            emp.age = request.POST.get('empage')
            emp.city = request.POST.get('empcity').lower()
            emp.mobileno = request.POST.get('empmobileno')
            emp.salary = request.POST.get('empsalary')

            emp.save()
            return HttpResponse("Employee Record Add Successfully.")
        elif 'btnsearch' in request.POST:
            id = request.POST.get('empid')
            emp = Employee.objects.get(id=id)
            d1 = {
                'emp':emp
            }
            return render(request, 'home.html', context=d1)

        elif 'btnupdate' in request.POST:
            id = request.POST.get('empid')
            emp = Employee.objects.get(id = id)
            
            emp.name = request.POST.get('empname').lower()
            emp.age = request.POST.get('empage')
            emp.city = request.POST.get('empcity').lower()
            emp.mobileno = request.POST.get('empmobileno')
            emp.salary = request.POST.get('empsalary')

            emp.save()
            return HttpResponse("Employee Record Update Successfully.")
        elif 'btndel' in request.POST:
            id = request.POST.get('empid')
            emp = Employee.objects.get(id = id)

            del emp
            return HttpResponse("Employee Record Delete Successfully.")

        elif 'btnshow' in request.POST:
            emps = Employee.objects.all()
            d1 = {
                'emps': emps
            }
            return render(request, 'Employee Record.html', context=d1)
        
def employee_record(request):
    # emps = Employee.objects.filter(name__startswith = 'a')
    emps = Employee.objects.all()
    return render(request, 'Employee Record.html', locals())