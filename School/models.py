from django.db import models


# Create your models here.
class Class(models.Model):
    name = models.CharField(max_length=10, null=False, blank=False)

    def __str__(self):
        return self.name


class Student(models.Model):
    Class = models.ForeignKey(Class, on_delete=models.PROTECT)
    name = models.CharField(max_length=15, null=False, blank=False)
    dob = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.name
