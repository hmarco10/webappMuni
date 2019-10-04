from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from user.models import User
from nichos.models import Student, reservacion, Predio, Propietario


def index(request, user_pk):
    template = 'nichos/index.html'
    context = {
        'user': User.objects.get(pk=user_pk),
    }
    return render(request, template, context)


def about(request, user_pk):
    template = 'nichos/about.html'
    context = {
        'user': User.objects.get(pk=user_pk),
    }
    return render(request, template, context)


def contact(request, user_pk):
    template = 'nichos/contacts.html'
    context = {
        'user': User.objects.get(pk=user_pk),
    }
    return render(request, template, context)


def students(request, user_pk):
    template = 'nichos/students.html'
    context = {
        'students': Student.objects.all(),
        'user': User.objects.get(pk=user_pk)
    }
    return render(request, template, context)


def create_student(request, user_pk):
    if request.method == 'POST':
        new_student = Student(
            name=request.POST['name'],
            last_name=request.POST['last_name'],
        )
        new_student.save()
        return HttpResponseRedirect(reverse('nichos:students', kwargs={'user_pk': user_pk}))
    elif request.method == 'GET':
        template = 'nichos/about.html'
        context = {
            'user': User.objects.get(pk=user_pk),
        }
        return render(request, template, context)
    return HttpResponse('No se puede guardar')


def edit_student(request, user_pk, student_pk):
    if request.method == 'POST':
        updated_student = Student.objects.get(pk=student_pk)
        updated_student.name = request.POST['name']
        updated_student.last_name = request.POST['last_name']
        updated_student.save()

        return HttpResponseRedirect(reverse('nichos:students', kwargs={'user_pk': user_pk}))

    elif request.method == 'GET':
        template = 'nichos/edit.html'
        context = {
            'student': Student.objects.get(pk=student_pk),
            'user': User.objects.get(pk=user_pk),
        }

        return render(request, template, context)
    return HttpResponse('Error, Method not allowed')


def delete_student(request, user_pk, student_pk):
    deleted_student = Student.objects.get(pk=student_pk)
    deleted_student.delete()
    return HttpResponseRedirect(reverse('nichos:students', kwargs={'user_pk': user_pk}))

def reservaciones(request, user_pk):
    template = 'nichos/students.html'
    context = {
        'reservacion': reservacion.objects.all(),
        'user': User.objects.get(pk=user_pk)
    }
    return render(request, template, context)


def crear_reservacion(request, user_pk):
    if request.method == 'POST':
        nueva_reservacion = reservacion(
            titular=request.POST['titular'],
            predio=request.POST['predio'],
            propietario=request.POST['propietario'],
            espacios=request.POST['espacios'],
            niveles=request.POST['niveles'],
            ornato=request.POST['ornato'],
            cancelado=request.POST['cancelado'],
            inspeccion=request.POST['inspeccion'],
            fecha=request.POST['fecha'],
        )
        nueva_reservacion.save()
        return HttpResponseRedirect(reverse('nichos:students', kwargs={'user_pk': user_pk}))
    elif request.method == 'GET':
        template = 'nichos/about.html'
        context = {
            'user': User.objects.get(pk=user_pk),
        }
        return render(request, template, context)
    return HttpResponse('No se puede guardar')