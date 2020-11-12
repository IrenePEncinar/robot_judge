from django import forms
from .models import Juicio

class JuicioForm(forms.Form):
    delito = forms.ChoiceField(choices=Juicio.TipoDelito.choices, label='Tipo de delito')
    antecedentes = forms.BooleanField(label='El acusado tenía antecedentes', required=False)
    supuestos = forms.ChoiceField(choices=Juicio.Supuesto.choices, label='Supuestos de hecho')
    procedencia = forms.ChoiceField(choices=Juicio.Procedencia.choices, label='Lugar de procedencia del acusado')
    sentencia = forms.ChoiceField(choices=Juicio.Sentencia.choices, label='Sentencia')
    nombre_juez = forms.CharField(max_length=200, label='Nombre del juez', required=False)