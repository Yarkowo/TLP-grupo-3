from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

TIPO_SEGMENTO = (
    ("C","Comunidad USM"),
    ("E","Estudiante"),
    ("P","Profesor"),
    ("J","Jefe de Carrera")
)
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
    ('OAI',"OAI")
    )    

class Evento(models.Model):
    fecha_inicio = models.DateTimeField()
    fecha_termino = models.DateTimeField()
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=300)
    
    tipo_tipo = models.CharField(max_length=10,choices=TIPO_TIPO)
    tipo_segmento = MultiSelectField(choices=TIPO_SEGMENTO,
                                max_length=10)
    def __str__(self) -> str:
        return self.titulo

class UsuarioSegmento(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo_segmento = models.CharField(max_length=10,choices=TIPO_SEGMENTO,default="C")
    def __str__(self):
        return self.usuario.username
    
