from django.db import models

# Create your models here.
class persona(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    edad = models.IntegerField()

    def __unicode__(self):
    	return "%s %s"%(self.nombre, self.apellido)