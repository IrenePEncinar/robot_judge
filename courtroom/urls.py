from django.urls import path
from . import views

urlpatterns = [
    path('', views.nuevo_juicio, name='nuevo_juicio'),
    path('guardar_juicio', views.guardar_juicio, name='guardar_juicio'),
    path('gracias', views.gracias, name='gracias'),
]
