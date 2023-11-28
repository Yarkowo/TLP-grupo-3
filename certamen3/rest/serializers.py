from rest_framework import fields,serializers
from nuestrapp.models import Evento,TIPO_SEGMENTO

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'
    tipo_segmento = fields.MultipleChoiceField(choices=TIPO_SEGMENTO)