from django.db import models

# Create your models here.


class TablaPostura(models.Model):
    id_principal = models.IntegerField()
    id_conductor = models.IntegerField()
    id_conductor2 = models.IntegerField()
    id_auxiliar = models.IntegerField()
    bus_id = models.IntegerField()
    conductor = models.CharField(max_length=200)
    conductor2 = models.CharField(max_length=200)
    auxiliar = models.CharField(max_length=200)
    bus = models.IntegerField()
    respuesta = models.TextField()

    class Meta:
        managed = True
        db_table = 'tablapostura'