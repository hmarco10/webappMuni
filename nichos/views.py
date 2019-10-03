from django.shortcuts import render, redirect

#vistas genericas para el crud

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import owner, Student, Subject

from django.urls import reverse
#from django.contrib import messages
#from django.contrib.messages.views import SuccessMessage
from django import forms 

from .forms import StudentForm, MascotaForm
# Create your views here.


def index(request):
    template = 'nichos/index.html'
    return render(request, template)


def about(request):
    template = 'nichos/about.html'
    return render(request, template)


def typography(request):
    template = 'nichos/typography.html'
    return render(request, template)


def contact(request):
    template = 'nichos/contacts.html'
    return render(request, template)


# CRUD

def list_student (request):
	student = Student.objects.all()
	return render (request, template_name= 'nichos/list_student.html', context = {'student':student})
	#return render (request, template_name= 'nichos/typography.html', context = {'student':student})

class StudentCreate(CreateView):
	model = Student
	form_class = StudentForm
	template_name = 'nichos/about.html'
	# template_name = 'nichos/typography.html'

	#def get_success_url(self):
	#	return reverse('nichos:list_student')

def mascota_view(request):
	if request.method == 'POST':
		form = MascotaForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('nichos:list_student')
	else:
		form = MascotaForm()
	
	return render(request,'nichos/about.html',{'form':form})

def mascota_edit(request, id_mascota):
	mascota = Student.objects.get(id=id_mascota)
	if request.method == 'GET':
		form = MascotaForm(instance=mascota)
	else: 
		form = MascotaForm(request.POST, instance=mascota)
		if form.is_valid():
			form.save()
		return redirect('nichos:list_student')
	return render(request,'nichos/about.html',{'form':form,'mascota': Student.objects.get(id=id_mascota)})