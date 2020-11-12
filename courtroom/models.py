from django.db import models

class Juicio(models.Model):
  class Meta:
    verbose_name_plural = "Juicios"
  
  class TipoDelito(models.TextChoices):
    ASESINATO = 'asesinato'
    HOMICIDIO = 'homicidio'
    ROBO = 'robo'
    HURTO = 'hurto'
    LESIONES = 'lesiones'

  class Supuesto(models.TextChoices):
    DINERO = 'dinero', 'El acusado recibió dinero'
    INCAPACIDAD = 'incapacidad', 'El acusado sufre incapacidad mental'
    DEFENSA_PROPIA = 'defensa_propia', 'Fue en defensa propia'
    HISTORIAL_ABUSOS = 'historial_abusos', 'Historial de abusos'
    MENOS_400 = 'menos_400', 'Menos de 400€'
    MAS_400 = 'más_400', 'Más de 400€'

  class Procedencia(models.TextChoices):
    MADRID = 'Madrid'
    BARCELONA = 'Barcelona'
    VALENCIA = 'Valencia'
    BILBAO = 'Bilbao'

  class Sentencia(models.TextChoices):
    ABSOLUCION = 'absolución', 'Absolución'
    MULTA = 'multa', 'Multa'
    CARCEL_2 = 'carcel_2', '2 años de cárcel'
    CARCEL_20 = 'carcel_20', '20 años de cárcel'

  class TipoDataset(models.TextChoices):
    TRAINING = 'training'
    TEST = 'test'
    
  id = models.AutoField(primary_key=True)
  delito = models.CharField(max_length=200, choices=TipoDelito.choices, verbose_name='Tipo de delito')
  antecedentes = models.BooleanField(verbose_name='El acusado tenía antecedentes')
  supuestos = models.CharField(max_length=200, choices=Supuesto.choices, verbose_name='Supuestos de hecho')
  procedencia = models.CharField(max_length=200, choices=Procedencia.choices, verbose_name='Lugar de procedencia del acusado')
  sentencia = models.CharField(max_length=200, choices=Sentencia.choices, verbose_name='Sentencia')
  nombre_juez = models.CharField(max_length=200, null=True, blank=True, verbose_name='Nombre del juez')
  dataset = models.CharField(max_length=200, choices=TipoDataset.choices, null=True, blank=True)
