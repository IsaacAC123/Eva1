from django.db import models
from django.utils import timezone

class Socio(models.Model):
    TIPO_VIVIENDA = [
        (1, 'Casa con patio Grande'),
        (2, 'Casa con Patio Pequeño'),
        (3, 'Casa sin patio'),
        (4, 'Departamento'),
    ]
    correo = models.EmailField()
    rut = models.CharField(max_length=15, verbose_name= 'RUT')
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length= 9, verbose_name='Telefono')
    ciudad = models.CharField(max_length=50, verbose_name='Ciudad')
    vivienda = models.IntegerField(choices=TIPO_VIVIENDA)

    def __str__(self):
        return self.correo 

# Create your models here.

class Postulante(models.Model):
    correo = models.EmailField(max_length=30)
    rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=9)
    region = models.CharField(max_length=100)
    comuna = models.CharField(max_length=100)
    tipo_vivienda = models.CharField(max_length=100)

class Listaperros(models.Model):
    TIPO_ESTADO = [
        (1, 'Disponible'),
        (2, 'Rescatado'),
        (3, 'Adoptado'),
        (4, 'En tratamiento medicos'),
    ]
    Nombre = models.CharField(max_length=20)
    Raza_predominante = models.CharField(max_length=50)
    Descripcion = models.CharField(max_length=1000)
    estado = models.IntegerField(choices=TIPO_ESTADO)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.Nombre, self. estado)
