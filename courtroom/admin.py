from django.contrib import admin, messages
from django.utils.translation import ngettext
from django.http import HttpResponse
import csv

from courtroom.models import Juicio

@admin.register(Juicio)
class JuicioAdmin(admin.ModelAdmin):
  list_per_page = 50
  list_display = ('nombre_juez', 'delito', 'antecedentes', 'supuestos', 'procedencia', 'sentencia', 'dataset')
  list_editable = ('dataset',)
  list_filter = ('dataset',)
  search_fields = ('nombre_juez',)
  list_display_links = ('delito', )
  actions = ('mark_as_training', 'mark_as_test', 'export_selected_as_csv')

  def mark_as_training(self, request, queryset):
    updated = queryset.update(dataset=Juicio.TipoDataset.TRAINING)
    self.message_user(request, ngettext(
      '%d juicio marcado como training',
      '%d juicios marcados como training',
      updated,
    ) % updated, messages.SUCCESS)
  mark_as_training.short_description = 'Marcar seleccionados como conjunto de TRAINING'

  def mark_as_test(self, request, queryset):
    updated = queryset.update(dataset=Juicio.TipoDataset.TEST)
    self.message_user(request, ngettext(
      '%d juicio marcado como test',
      '%d juicios marcados como test',
      updated,
    ) % updated, messages.SUCCESS)
  mark_as_test.short_description = 'Marcar seleccionados como conjunto de TEST'

  def export_selected_as_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    dataset = request.GET.get('dataset__exact')
    print(dataset)
    response['Content-Disposition'] = f'attachment; filename="{dataset}_set.csv"'

    writer = csv.writer(response)

    writer.writerow(['delito', 'antecedentes', 'supuestos', 'procedencia', 'sentencia'])

    for item in queryset:
      writer.writerow([item.delito, item.antecedentes, item.supuestos, item.procedencia, item.sentencia])

    writer.writerow(['hurto', 'False', 'menos_400', 'Barcelona', 'multa'])
    writer.writerow(['robo', 'True', 'más_400', 'Barcelona', 'carcel_2'])
    writer.writerow(['asesinato', 'False', 'incapacidad', 'Madrid', 'carcel_2'])
    writer.writerow(['homicidio', 'False', 'defensa_propia', 'Bilbao', 'absolución'])
    writer.writerow(['lesiones', 'False', 'defensa_propia', 'Bilbao', 'absolución'])
    writer.writerow(['lesiones', 'True', 'historial_abusos', 'Valencia', 'carcel_20'])
    writer.writerow(['asesinato', 'True', 'dinero', 'Madrid', 'carcel_20'])

    return response

  export_selected_as_csv.short_description = 'Exportar juicios seleccionados como CSV'
  
