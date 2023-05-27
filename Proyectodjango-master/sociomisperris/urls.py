from django.urls import path
from sociomisperris import views
from act2.vista import home

urlpatterns = [
    path('', vista.home)
]