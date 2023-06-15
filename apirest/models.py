from django.db import models

# Create your models here.
class Sensores(models.Model):
    temperatura = models.FloatField()
    peso = models.FloatField()
    humedad = models.IntegerField()
class Lecturas(models.Model):
    key = models.TextField()
    value = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)
#date_updated = models.DateTimeField(auto_now=True) #Filaque almacena la actualizacion automatica de datos