from django.shortcuts import render
from .models import Evento

# Create your views here.

def index(request):

    respuestaSegmento = request.GET.get('Segmento')
    respuestaTipo = request.GET.get('Tipo')

    segmentos = ["Comunidad_USM","Estudiante","Profesor","Jefe_de_Carrera"]
    tipos = ["Vacaciones","Feriado","Suspensión_de_actividades","Suspensión_de_actividades_PM","Periodo_Lectivo","Suspensión_de_evaluaciones","Ceremonia","EDDA","Evaluación","Ayudantías","Hito_Académico","Secretaría_Académica","OAI",]
    
    #filtro
    if (respuestaSegmento == 'Segmento' or respuestaSegmento == None) and (respuestaTipo == 'Tipo' or respuestaTipo == None): #Segmento none / Tipo none
        actividades = Evento.objects.all()
    elif (respuestaSegmento != 'Segmento') and (respuestaTipo != 'Tipo'): #Segmento [X] / Tipo [X]
        actividades = Evento.objects.filter(tipo_tipo=respuestaTipo).filter(segmento_segmento=respuestaSegmento)
    elif (respuestaSegmento != 'Segmento') and (respuestaTipo == 'Tipo' or respuestaTipo == None): #Segmento [X] / Tipo none
        actividades = Evento.objects.filter(tipo_segmento=respuestaSegmento)
    elif (respuestaSegmento == 'Segmento' or respuestaSegmento == None) and (respuestaTipo != 'Tipo'): #Segmento none / Tipo [X]
        actividades = Evento.objects.filter(tipo_tipo=respuestaTipo)

    data={
        "actividades":actividades,
        "Segmentos":segmentos,
        "Tipos":tipos,
        "respuestaSegmento":respuestaSegmento,
        "respuestaTipo":respuestaTipo,
    }
    return render(request, 'nuestrapp/base.html',data)