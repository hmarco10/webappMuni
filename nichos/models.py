from django.db import models
from django.contrib import admin

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

    def __str__(self):
        return self.name


class Registration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    schedule_time = models.TimeField()

    def __str__(self):
        return self.student.name + self.subject.name

class Propietario(models.Model):
    nombre = models.CharField(max_length=250)
    dpi = models.IntegerField()
    telefono = models.CharField(max_length=8)
    direccion = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre


class Predio(models.Model):
    largo = models.FloatField()
    ancho = models.FloatField()
    nomenclatura = models.CharField(max_length=10)
    #propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)
    def __str__(self):
        return self.nomenclatura
    
class reservacion(models.Model):
    titular = models.CharField(max_length=250)
    espacios = models.IntegerField()
    niveles = models.IntegerField()
    ornato = models.BooleanField()
    cancelado = models.BooleanField()
    inspeccion = models.BooleanField()
    fecha = models.DateTimeField(auto_now_add=True)
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)
    predio = models.ForeignKey(Predio, on_delete=models.CASCADE)

    def __str__(self):
        return 'Titular: '+ self.titular + 'Espacios: '+ str(self.espacios)




    