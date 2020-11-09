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
    DINERO = 'el acusado recibió dinero'
    INCAPACIDAD = 'el acusado sufre incapacidad mental'
    DEFENSA_PROPIA = 'fue en defensa propia'
    HISTORIAL_ABUSOS = 'historial de abusos'
    MENOS_400 = 'menos de 400€'
    MAS_400 = 'menos de 400€'

  class Procedencia(models.TextChoices):
    MADRID = 'Madrid'
    BARCELONA = 'Barcelona'
    VALENCIA = 'Valencia'
    BILBAO = 'Bilbao'

  class Sentencia(models.TextChoices):
    ABSOLUCION = 'absolución'
    MULTA = 'multa'
    CARCEL_2 = '2 años de cárcel'
    CARCEL_20 = '20 años de cárcel'
    
  id = models.AutoField(primary_key=True)
  delito = models.CharField(max_length=200, choices=TipoDelito.choices, verbose_name='Tipo de delito')
  antecedentes = models.BooleanField(verbose_name='Antecendentes del acusado')
  supuestos = models.CharField(max_length=200, choices=Supuesto.choices, verbose_name='Supuestos de hecho')
  procedencia = models.CharField(max_length=200, choices=Procedencia.choices, verbose_name='Lugar de procedencia del acusado')
  sentencia = models.CharField(max_length=200, choices=Sentencia.choices, verbose_name='Sentencia')
  nombre_juez = models.CharField(max_length=200, null=True, blank=True)
