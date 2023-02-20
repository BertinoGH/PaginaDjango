from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('quehacer/', views.quehacer, name='quehacer'),
    path('origen/', views.origen, name='origen'),
    path('formas/', views.formas, name='formas'),
    path('campañas/', views.campañas, name='campañas'),
    path('prueba/', views.prueba, name='prueba'),
]