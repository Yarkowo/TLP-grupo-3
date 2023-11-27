from django.shortcuts import render

# Create your views here.

def index(request):

    respuestaSegmento = request.GET.get('Segmento')
    respuestaTipo = request.GET.get('Tipo')

    segmentos = ["Comunidad_USM","Estudiante","Profesor","Jefe_de_Carrera"]
    tipos = ["Vacaciones","Feriado","Suspensión_de_actividades","Suspensión_de_actividades_PM","Periodo_Lectivo","Suspensión_de_evaluaciones","Ceremonia","EDDA","Evaluación","Ayudantías","Hito_Académico","Secretaría_Académica","OAI",]
    data={
        "Segmentos":segmentos,
        "Tipos":tipos,
        "respuestaSegmento":respuestaSegmento,
        "respuestaTipo":respuestaTipo,
    }
    return render(request, 'nuestrapp/base.html',data)