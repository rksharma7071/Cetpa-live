from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    city = models.CharField(max_length=100)
    mobileno = models.CharField(max_length=50)
    salary = models.IntegerField()

    def __str__(self):
        return self.name