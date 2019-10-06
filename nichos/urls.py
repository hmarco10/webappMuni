from django.urls import path
from nichos import views


app_name = 'nichos'
urlpatterns = [
    path('index/<int:user_pk>/', views.index, name='index'),
    path('about/<int:user_pk>/', views.about, name='about'),
    path('contacts/<int:user_pk>/', views.contact, name='contacts'),
    path('', views.landing_page, name='landing'),
    path('contact1/', views.contact1, name='contact1'),
    path('crear_reservacion/<int:user_pk>/', views.crear_reservacion, name='crear_reservacion'),

    #path('crear_reservacion/<int:user_pk>/', views.crear_reservacion, name='crear_reservacion'),
   # path('reservaciones/<int:user_pk>/', views.show_reservation, name='show_reservation'),
]