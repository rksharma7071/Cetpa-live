from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    pic = models.ImageField(upload_to='student')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dob = models.DateField()
    mobileno = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, null=True, blank=True)

    def __str__(self):
        return self.name


class PaymentDetails(models.Model):
    amount = models.IntegerField()
    payment_mode = models.CharField(max_length=100, choices=[('Cash','Cash'), ('Debit Card','Debit Card'), ('Credit Card','Credit Card'),('UPI','UPI')])
    payment_date = models.DateTimeField(auto_now=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
