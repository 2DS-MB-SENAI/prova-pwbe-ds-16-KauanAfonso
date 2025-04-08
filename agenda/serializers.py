from rest_framework import serializers
from .models import Servico,Agendamento

class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = ['nome', 'duracao', 'preco']


class AgendamentoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Agendamento
        fields = '__all__'