from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from user.models import User
from nichos.models import Reservation, Predio, Propietario


def landing_page(request):
    template = 'nichos/landing_page.html'
    return render(request, template)

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


def contact1(request):
    template = 'nichos/contact1.html'
    return render(request, template)


def show_reservation(request, user_pk):
    template = 'nichos/students.html'
    context = {
        'reservaciones': Propietario.objects.all(),
        'user': User.objects.get(pk=user_pk)
    } 
    return render(request, template, context)

def crear_reservacion(request, user_pk):
    if request.method == 'POST':
        post_predio = Predio.objects.get(pk=request.POST['predio'])
        post_propietario = Propietario.objects.get(pk=request.POST['propietario'])
        nueva_reservacion = Reservation(
            titular=request.POST['titular'],
            espacios=request.POST['espacios'],
            niveles=request.POST['niveles'],
            ornato=request.POST['ornato'],
            cancelado=request.POST['cancelado'],
            inspeccion=request.POST['inspeccion'],
            fecha=request.POST['fecha'],
            predio = post_predio,
            propietario= post_propietario,
        )
        nueva_reservacion.save()
        return HttpResponseRedirect(reverse('nichos:index', kwargs={'user_pk': user_pk}))
    elif request.method == 'GET':
        template = 'nichos/about.html'
        context = {
            'user': User.objects.get(pk=user_pk),
            'predios': Predio.objects.all(),
            'propietarios': Propietario.objects.all(),
        }
        return render(request, template, context)
    return HttpResponse('No se puede guardar')