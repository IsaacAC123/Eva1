from django.db import models

# Create your models here.
class Adoptante(models.Model):
    correo = models.EmailField(max_length=30)
    rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length=50)
    fecha_naci = models.DateField()
    contacto = models.CharField(max_length=9)
    regionS = models.CharField(max_length=50)
    comunaS = models.CharField(max_length=50)
    tipo_vivienda = models.CharField(max_length=50)
    class Meta:
        app_label = 'myapp'
