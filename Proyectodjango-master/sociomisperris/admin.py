from django.contrib import admin
from .models import Socio
from .models import Postulante
from sociomisperris.models import Listaperros
admin.site.register(Socio)
# Register your models here.
admin.site.register(Postulante)

admin.site.register(Listaperros)