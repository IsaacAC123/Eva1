from django.shortcuts import render
from django.http import HttpResponseRedirect
from sociomisperris.models import Postulante
def index(request):
    return render(request, 'formulario.html')
    
    
    
def formulario(request):    
    if request.method == 'POST':
        correo = request.POST['correo']
        rut = request.POST['RUT']
        nombre = request.POST['Nombre']
        fecha_nacimiento = request.POST['Fecha_naci']
        telefono = request.POST['contacto']
        region = request.POST['region']
        comuna = request.POST['comuna']
        tipo_vivienda = request.POST['tipovivienda']
        postulante = Postulante(correo=correo, rut=rut, nombre=nombre, fecha_nacimiento=fecha_nacimiento, telefono=telefono, region=region, comuna=comuna, tipo_vivienda=tipo_vivienda)
        postulante.save()
        return HttpResponseRedirect('/formulario/')
    else:
        return render(request, 'formulario.html')