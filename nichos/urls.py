from django.urls import path
from nichos import views


app_name = 'nichos'
urlpatterns = [
    path('index/<int:user_pk>/', views.index, name='index'),
    path('about/<int:user_pk>/', views.about, name='about'),
    path('contacts/<int:user_pk>/', views.contact, name='contacts'),
    path('create_student/<int:user_pk>/', views.create_student, name='create_student'),
    path('crear_reservacion/<int:user_pk>/', views.crear_reservacion, name='crear_reservacion'),
    path('students/<int:user_pk>/', views.students, name='students'),
    path('edit_student/<int:user_pk>/<int:student_pk>/', views.edit_student, name='edit_student'),
    path('delete_student/<int:user_pk>/<int:student_pk>/', views.delete_student, name='delete_student'),
    path('reservaciones/<int:user_pk>/', views.show_reservation, name='show_reservation'),

]