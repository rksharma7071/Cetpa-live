from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group,Permission
from django.contrib.auth.decorators import login_required
from .forms import StudentRegistrationForm


def view_home(request):
    return render(request, 'LMS/home.html')





@login_required(login_url='login')
def view_secure1(request):
    return render(request, 'LMS/secure1.html')


@login_required(login_url='login')
def view_secure2(request):
    return render(request, 'LMS/secure2.html')


def view_unsecure1(request):
    return render(request, 'LMS/unsecure1.html')


def view_unsecure2(request):
    return render(request, 'LMS/unsecure2.html')


def view_logout(request):
    logout(request)
    return redirect('login')