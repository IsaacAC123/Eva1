from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FormularioAdopcion
from .models import Adopcion

def guardar_datos(request):
    if request.method == 'POST':
        formulario = FormularioAdopcion(request.POST)
        if formulario.is_valid():
            correo = formulario.cleaned_data['correo']
            RUT = formulario.cleaned_data['RUT']
            Nombre = formulario.cleaned_data['Nombre']
            Fecha = formulario.cleaned_data['Fecha']
            contacto = formulario.cleaned_data['contacto']
            tipovivienda = formulario.cleaned_data['tipovivienda']
            adopcion = Adopcion(correo=correo, RUT=RUT, Nombre=Nombre, Fecha=Fecha, contacto=contacto, tipovivienda=tipovivienda)
            adopcion.save()
            return HttpResponseRedirect('/formulario/gracias/')
    else:
        formulario = FormularioAdopcion()
    return render(request, 'formulario.html', {'formulario': formulario})
