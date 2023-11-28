from django.db import models
from django.contrib.auth.models import User
TIPO_SEGMENTO = (
    ("C","Comunidad USM"),
    ("E","Estudiante"),
    ("P","Profesor"),
    ("J","Jefe de Carrera")
)

class Evento(models.Model):
    fecha_inicio = models.DateTimeField()
    fecha_termino = models.DateTimeField()
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=300)
    TIPO_TIPO = (
    ("V","Vacaciones"),
    ("F","Feriado"),
    ("S1","Suspensión de actividades"),
    ("S2", "Suspensión de actividades PM"),
    ("P","Periodo Lectivo")
    #Faltan mas
    )    
    tipo_tipo = models.CharField(max_length=10,choices=TIPO_TIPO,default="F")
    tipo_segmento = models.CharField(max_length=10,choices=TIPO_SEGMENTO,default="C")
    def __str__(self) -> str:
        return self.titulo

class UsuarioSegmento(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo_segmento = models.CharField(max_length=10,choices=TIPO_SEGMENTO,default="C")
    def __str__(self):
        return self.usuario.username
    
