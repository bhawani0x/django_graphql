from django.db import models


# Create your models here.
class Class(models.Model):
    name = models.CharField(max_length=10, null=False, blank=False)
    Class_teacher_name = models.CharField(max_length=10, null=True, blank=True)
    class_teacher_number = models.IntegerField(null=True, blank=True, max_length=10)

    def __str__(self):
        return self.name


class Student(models.Model):
    Class = models.ForeignKey(Class, on_delete=models.PROTECT)
    first_name = models.CharField(max_length=15, null=False, blank=False)
    last_name = models.CharField(max_length=15, null=False, blank=False)
    dob = models.DateField(auto_now_add=False)
    Father_name = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
