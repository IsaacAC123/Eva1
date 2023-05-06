from django import forms

class FormularioAdopcion(forms.Form):
    correo = forms.EmailField(max_length=30, required=True)
    RUT = forms.CharField(max_length=12, required=True)
    Nombre = forms.CharField(max_length=50, required=True)
    Fecha = forms.DateField(required=True)
    contacto = forms.CharField(max_length=9, required=True)
    tipovivienda = forms.ChoiceField(choices=[('Casa con patio grande', 'Casa con patio grande'),
                                              ('Casa con patio chico', 'Casa con patio chico'),
                                              ('Casa sin patio', 'Casa sin patio'),
                                              ('Departamento', 'Departamento')],
                                     required=True)
