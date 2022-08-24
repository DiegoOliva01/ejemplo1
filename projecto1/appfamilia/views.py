from django.shortcuts import render
from appfamilia.models import Familiar
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def individuo (request):
    

    persona_1=Familiar(nombre="Humberto",apellido="Oliva",edad=59,trabajo="capataz de limpieza,fabrica Palmar",hijos=5,nacimiento="1963-11-13")
    persona_1.save()

    persona_2=Familiar(nombre="Adriana",apellido="Almada",edad=55,trabajo="ama de casa",hijos=5,nacimiento="1968-10-5")
    persona_2.save()

    persona_3=Familiar(nombre="Lucas",apellido="Oliva",edad=35,trabajo="repartidor de bidones de agua,empresa acuavita",hijos=1,nacimiento="1986-10-5")
    persona_3.save()

    persona_4=Familiar(nombre="Matias",apellido="Oliva",edad=31,trabajo="puesto en administracion del puesto los gringos,mercado de abasto",hijos=1,nacimiento="1989-8-11")
    persona_4.save()


    plantilla=loader.get_template("template1.html")

    diccionario={"familiares:"[persona_1,persona_2,persona_3,persona_4]}

    documento=plantilla.render(diccionario)

    return HttpResponse(documento)