from django.urls import path
from nichos import views
from .views import mascota_view, mascota_edit


app_name = 'nichos'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    #path('typography/', views.typography, name='typography'),
    #path('typography/', views.StudentCreate.as_view() , name='create_student'),
    path('list_student/', views.list_student, name = 'list_student'),
    path('create_student/', mascota_view, name='mascota_crear'),
    path('editar/<int:id_mascota>/', mascota_edit, name='mascota_editar'),
    path('contact-us/', views.contact, name='contact-us'),
]