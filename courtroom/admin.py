from django.contrib import admin
from courtroom.models import Juicio

@admin.register(Juicio)
class JuicioAdmin(admin.ModelAdmin):
  list_per_page = 50
  list_display = ('nombre_juez', 'delito', 'antecedentes', 'supuestos', 'procedencia', 'sentencia', 'dataset')
  list_editable = ('dataset',)
