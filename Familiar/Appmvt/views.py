from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from Appmvt.models import Familiares


# Create your views here.

# Se genera función de vista
def listaFamiliares(request):

    dato1 = Familiares(nombre ="Walter", edad=53, fecha="23-02-1982")

    dato2 = Familiares(nombre ="Ricardo", edad=78, fecha="1-04-1943")

    dato3 = Familiares(nombre ="Indiana", edad=30, fecha="5-11-1992")

    return render(request, r"C:\Users\Piruu\Desktop\DESAFIO_FAMILIAR\Familiar\Appmvt\Templete\index.html", {"familia":[dato1,dato2,dato3]})




