from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    # nueva ruta 'servicios/' → función views.servicios → alias 'servicios'
    path('servicios/', views.servicios, name='servicios'),
]