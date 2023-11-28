from .models import Evento, User, UsuarioSegmento
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

# Create your views here.
#a
def index(request):

    respuestaSegmento = request.GET.get('Segmento')
    respuestaTipo = request.GET.get('Tipo')
    mostrar = False
    for u in UsuarioSegmento.objects.all():
        if u.usuario == request.user:
            segmento_usuario = u.tipo_segmento
            if (segmento_usuario in ["P","J"]):
                mostrar = True

    Usuario = request.user

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
    
    #filtro
    if (respuestaSegmento == 'Segmento' or respuestaSegmento == None) and (respuestaTipo == 'Tipo' or respuestaTipo == None): #Segmento none / Tipo none
        actividades = Evento.objects.all()

    elif (respuestaSegmento != 'Segmento') and (respuestaTipo != 'Tipo'): #Segmento [X] / Tipo [X]
        actividades = Evento.objects.filter(tipo_tipo__contains=tipos[respuestaTipo]).filter(tipo_segmento__contains=segmentos[respuestaSegmento])

    elif (respuestaSegmento != 'Segmento') and (respuestaTipo == 'Tipo' or respuestaTipo == None): #Segmento [X] / Tipo none
        actividades = Evento.objects.filter(tipo_segmento__contains=segmentos[respuestaSegmento])

    elif (respuestaSegmento == 'Segmento' or respuestaSegmento == None) and (respuestaTipo != 'Tipo'): #Segmento none / Tipo [X]
        actividades = Evento.objects.filter(tipo_tipo__contains=tipos[respuestaTipo])

    #fin_filtro
    actividades_siguientes = []
    c=0
    if (mostrar==True):
        for event in Evento.objects.filter(tipo_segmento__contains=segmento_usuario).order_by('-fecha_termino').reverse():
            if (c  < 3):
                actividades_siguientes.append(event)
            c+=1
        

    data={
        "actividades":actividades.order_by('-fecha_inicio').reverse(),
        "Segmentos":segmentos,
        "Tipos":tipos,
        "respuestaSegmento":respuestaSegmento,
        "respuestaTipo":respuestaTipo,
        "Usuario":Usuario,
        "mostrar":mostrar,
        "actividades_siguientes":actividades_siguientes,
    }
    return render(request, 'nuestrapp/base.html',data)

def login(request):
    users = []
    nombre = request.GET.get('usuario')
    contraseña = request.GET.get('contraseña')
    logeado = 1
    if (nombre != None) and (contraseña!=None):
        logeado = 3

    for u in User.objects.all():
        users.append((u.username,u.password))

    for usuario in users:
        if usuario[0] == nombre:
            if check_password(contraseña,usuario[1]):
                logeado = 2
    data={
        "Usuarios":users,
        "con":contraseña,
        "nombre":nombre,
        "si":logeado
    }
    return render(request,"nuestrapp/login.html",data)
