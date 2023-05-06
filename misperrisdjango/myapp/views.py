from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Adoptante

# Create your views here.
def guardar_datos(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        rut = request.POST.get('RUT')
        nombre = request.POST.get('Nombre')
        fecha_naci = request.POST.get('Fecha')
        contacto = request.POST.get('contacto')
        regionS = request.POST.get('regionValue')
        comunaS = request.POST.get('comunaValue')
        tipo_vivienda = request.POST.get('tipovivienda')
        Adoptante = Adoptante(correo=correo, rut=rut, nombre=nombre, fecha_naci=fecha_naci, contacto=contacto, regionS=regionS, comunaS=comunaS, tipo_vivienda=tipo_vivienda)
        Adoptante.save()
        return HttpResponseRedirect('Formulario enviado!.')
    else:
        return render(request, 'formulario.html')