from django.contrib import admin
from .models import owner, Subject, Student, Registration, Propietario, Predio, reservacion


# Register your models here.

admin.site.register(owner)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Registration)
admin.site.register(Propietario)
admin.site.register(Predio)
admin.site.register(reservacion)