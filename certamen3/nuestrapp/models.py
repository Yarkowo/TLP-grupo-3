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
    ('V',"Vacaciones"),
    ('F',"Feriado"),
    ('SA',"Suspensión_de_actividades"),
    ('SAPM',"Suspensión_de_actividades_PM"),
    ('PL',"Periodo_Lectivo"),
    ('SE',"Suspensión_de_evaluaciones"),
    ('C',"Ceremonia"),
    ('EDDA',"EDDA"),
    ('E',"Evaluación"),
    ('A',"Ayudantías"),
    ('HA',"Hito_Académico"),
    ('SECA',"Secretaría_Académica"),
    ('OAI',"OAI"),
    )    
    tipo_tipo = models.CharField(max_length=10,choices=TIPO_TIPO,default="F")
    tipo_segmento = models.CharField(max_length=10,choices=TIPO_SEGMENTO,default="C")

    # def __str__(tipo_tipo):
    #    return f"{self.first_name} {self.last_name}"

class UsuarioSegmento(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo_segmento = models.CharField(max_length=10,choices=TIPO_SEGMENTO,default="C")
    def __str__(self):
        return self.usuario
    