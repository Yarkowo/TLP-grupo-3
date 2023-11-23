from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
# Create your views here.

def index(request):

    respuestaSegmento = request.GET.get('Segmento')
    respuestaTipo = request.GET.get('Tipo')

    segmentos = ["Comunidad USM","Estudiante","Profesor","Jefe de Carrera"]
    tipos = ["Vacaciones","Feriado","Suspensión de actividades","Suspensión de actividades PM","Periodo Lectivo","Suspensión de evaluaciones","Ceremonia","EDDA","Evaluación","Ayudantías","Hito Académico","Secretaría Académica","OAI",]
    data={
        "Segmentos":segmentos,
        "Tipos":tipos
    }
    return render(request, 'nuestrapp/base.html',data)