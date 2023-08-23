from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User, Group,Permission
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *


def view_register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        user_form = UserCreationForm(request.POST, label_suffix='')
        student_form = StudentForm(request.POST, label_suffix='')
        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save()
            user.is_staff = True
            user.save()
            g1 = Group.objects.get(id=1)
            user.groups.add(g1)
            student = student_form.save(commit=False)
            student.user = user
            student.save()
            return HttpResponse('<h1>User Registration Successfully.')
    else:
        user_form = UserCreationForm(label_suffix='')
        student_form = StudentForm(label_suffix='')

    return render(request, 'myapp/register.html', locals())


def view_login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':

        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('secure1')
    else:
        form = AuthenticationForm()
    return render(request, 'myapp/login.html', locals())


def all_student(request):
    students = Student.objects.all()
    d1 = {'students':students}
    return render(request, 'myapp/all_student.html', context=d1)


def all_payment(request):
    payments = PaymentDetails.objects.all()
    d1 = {'payments':payments}
    return render(request, 'myapp/all_payment.html', context=d1)


def student_payment(request):
    if request.method == "GET":
        return render(request, 'myapp/student_payment.html')

    elif request.method == "POST":
        try:
            id = request.POST.get('id')
            student = Student.objects.get(id = id)
            payments = student.paymentdetails_set.all()

            d1 = {'student': student, 'payments':payments}
        except Student.DoesNotExist:
            d1 = {'error': 'Student Does not exist.'}
    return render(request, 'myapp/student_payment.html', context=d1)


def student_reg(request):
    if request.method == "GET":
        frm_unbound = StudentForm()
        d1 = {'form':frm_unbound}
        return render(request, 'myapp/student_reg.html', context=d1)

    elif request.method == 'POST':
        frm_bound = StudentForm(request.POST, files=request.FILES)
        if frm_bound.is_valid:
            frm_bound.save()
            return HttpResponse("Student Added Successfully.")
        else:
            d1 = {'form':frm_bound}
        return render(request, 'myapp/student_reg.html', context=d1)


def all_courses(request):
    courses = Course.objects.all()
    d1 = {'courses':courses}
    return render(request, 'myapp/all_courses.html', context=d1)


def course_reg(request):
    if request.method == "GET":
        frm_unbound = CourseForm()
        d1 = {'form':frm_unbound}
        return render(request, 'myapp/course_reg.html', context=d1)

    elif request.method == 'POST':
        frm_bound = CourseForm(request.POST)
        if frm_bound.is_valid:
            frm_bound.save()
            return HttpResponse("Course Added Successfully.")
        else:
            d1 = {'form':frm_bound}
        return render(request, 'myapp/course_reg.html', context=d1)


def PaymentDetails_reg(request):
    if request.method == "GET":
        frm_unbound = PaymentDetailsForm()
        d1 = {'form':frm_unbound}
        return render(request, 'myapp/payment_registration.html', context=d1)

    elif request.method == 'POST':
        frm_bound = PaymentDetailsForm(request.POST)
        if frm_bound.is_valid:
            frm_bound.save()
            return HttpResponse("Payment Added Successfully.")
        else:
            d1 = {'form':frm_bound}
        return render(request, 'myapp/payment_registration.html', context=d1)


def course_student(request):
    if request.method == "GET":
        return render(request, 'myapp/course_student.html')

    elif request.method == "POST":
        try:
            cid = request.POST.get('id')
            course = Course.objects.get(id=cid)
            students = course.students.all()

            d1 = {'course': course, 'students': students}
        except Course.DoesNotExist:
            d1 = {'error': 'Course Does not exist.'}
    return render(request, 'myapp/course_student.html', context=d1)



def view_show_student(request, id):
    stu = Student.objects.get(id=id)
    d1 = {'stu':stu}
    return render(request, 'myapp/showstu.html', context=d1)