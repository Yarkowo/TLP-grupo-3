from django.shortcuts import render
from .models import Evento

# Create your views here.

def index(request):

    respuestaSegmento = request.GET.get('Segmento')
    respuestaTipo = request.GET.get('Tipo')

    segmentos={"Comunidad_USM":'C',
                "Estudiante":'E',
                "Profesor":'P',
                "Jefe_de_Carrera":'J',
            }
    tipos = {"Vacaciones":'V',
            "Feriado":'F',
            "Suspensión_de_actividades":'SA',
            "Suspensión_de_actividades_PM":'SAPM',
            "Periodo_Lectivo":'PL',
            "Suspensión_de_evaluaciones":'SE',
            "Ceremonia":'C',
            "EDDA":'EDDA',
            "Evaluación":'E',
            "Ayudantías":'A',
            "Hito_Académico":'HA',
            "Secretaría_Académica":'SECA',
            "OAI":'OAI',
        }
    
    #en cuashro mami en cuashor

    #filtro
    if (respuestaSegmento == 'Segmento' or respuestaSegmento == None) and (respuestaTipo == 'Tipo' or respuestaTipo == None): #Segmento none / Tipo none
        actividades = Evento.objects.all()

    elif (respuestaSegmento != 'Segmento') and (respuestaTipo != 'Tipo'): #Segmento [X] / Tipo [X]
        actividades = Evento.objects.filter(tipo_tipo=tipos[respuestaTipo]).filter(tipo_segmento=segmentos[respuestaSegmento])

    elif (respuestaSegmento != 'Segmento') and (respuestaTipo == 'Tipo' or respuestaTipo == None): #Segmento [X] / Tipo none
        actividades = Evento.objects.filter(tipo_segmento=segmentos[respuestaSegmento])

    elif (respuestaSegmento == 'Segmento' or respuestaSegmento == None) and (respuestaTipo != 'Tipo'): #Segmento none / Tipo [X]
        actividades = Evento.objects.filter(tipo_tipo=tipos[respuestaTipo])

    #fin_filtro

    data={
        "actividades":actividades,
        "Segmentos":segmentos,
        "Tipos":tipos,
        "respuestaSegmento":respuestaSegmento,
        "respuestaTipo":respuestaTipo,
    }
    return render(request, 'nuestrapp/base.html',data)