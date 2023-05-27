from django.urls import path
from sociomisperris import views
from act2.vista import home
from act2.vista import registrarperros
from sociomisperris.views import registrarperros

urlpatterns = [
    path('', vista.home)
    path('registrarperros/', registrarperros, name='registrarperros')
]