from django.shortcuts import render, redirect

from .models import Juicio
from .forms import JuicioForm


def nuevo_juicio(request):
    f = JuicioForm()
    return render(request, 'index.html', {'form': f})

def guardar_juicio(request):
    # Obtenemos los datos que ha rellenado el usuario en el formulario
    f = JuicioForm(request.POST)

    # Si los datos son válidos, los procesamos para guardarlos en la base de datos
    # La función is_valid() valida los datos del formulario y los almacena en la
    # variable "cleaned_data"
    if f.is_valid():

        j = Juicio()
        j.delito = f.cleaned_data['delito']
        j.antecedentes = f.cleaned_data['antecedentes']
        j.supuestos = f.cleaned_data['supuestos']
        j.procedencia = f.cleaned_data['procedencia']
        j.sentencia = f.cleaned_data['sentencia']
        j.nombre_juez = f.cleaned_data['nombre_juez']
        j.save()

        return redirect('/gracias')

    # Si los datos no son válidos, volvemos a mostrar el formulario
    else:
        return render(request, 'index.html', {'form': f})


def gracias(request):
    return render(request, 'gracias.html')