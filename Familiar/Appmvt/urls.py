from django.urls import path
from Appmvt.views import listaFamiliares

urlpatterns = [
        path("", listaFamiliares),
]