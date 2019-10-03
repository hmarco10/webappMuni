from django.db import models

# Create your models here.

class owner(models.Model):
    name = models.CharField(max_length=250)
    dpi = models.IntegerField()
    phone = models.CharField(max_length=13)
    address= models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Subject (models.Model):
    name = models.CharField(max_length=250)
    number_credits = models.IntegerField()

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    subject_student = models.ManyToManyField(Subject)

    def __str__(self):
        return self.name