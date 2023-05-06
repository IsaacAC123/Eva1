from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Adoptante

# Create your views here.
def guardar_datos(request):
    if request.method == 'POST':
        Adoptante = Adoptante()
        Adoptante.correo = request.POST.get('correo')
        Adoptante.RUT = request.POST.get('RUT')
        Adoptante.nombre_completo = request.POST.get('Nombre')
        Adoptante.fecha_nacimiento = request.POST.get('Fecha')
        Adoptante.telefono = request.POST.get('contacto')
        Adoptante.region = request.POST.get('regionValue')
        Adoptante.comuna = request.POST.get('comunaValue')
        Adoptante.tipo_vivienda = request.POST.get('tipovivienda')
        Adoptante.save()
        return redirect('views.py')
    else:
        return render(request, 'formulario.html')