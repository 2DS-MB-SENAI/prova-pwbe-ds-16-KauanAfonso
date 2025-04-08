from django.shortcuts import render
from . serializers import ServicoSerializer, AgendamentoSerializer
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Servico, Agendamento
# Create your views here.



'''
Função para POST E GET de um serviço 
a função lida com os serviços

'''
@api_view(['GET', "POST"])
def lidar_servico(request,pk=None):

    if request.method == "GET":
        if pk is not None:
            try:
                servico = Servico.objects.get(pk=pk)
                serializer = ServicoSerializer(servico, many=False)
                return Response({"Sucesso": []}, status=status.HTTP_200_OK)
            except Servico.DoesNotExist:
                return Response({"ERRO": "Não encontrado"}, status = status.HTTP_404_NOT_FOUND)
        else:
            servico = Servico.objects.all()
            serializer = ServicoSerializer(servico, many=True)
            return Response({"Sucesso": serializer.data}, status=status.HTTP_200_OK)

    if request.method == "POST":
        serializer = ServicoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Sucesso": "Serviço criado"}, status=status.HTTP_201_CREATED)
        return Response({"ERRO": serializer.errors},status=status.HTTP_400_BAD_REQUEST)
                

'''
Função para POST E GET de um serviço 
a função lida com os agendamentos

'''

@api_view(['GET', "POST"])
def lidar_agendamento(request,pk=None):

    if request.method == "GET":
        if pk is not None:
            try:
                agendamento = agendamento.objects.get(pk=pk)
                serializer = AgendamentoSerializer(agendamento, many=False)
                return Response({"Sucesso": serializer.data}, status=status.HTTP_200_OK)
            except agendamento.DoesNotExist:
                return Response({"ERRO": "Não encontrado"}, status = status.HTTP_404_NOT_FOUND)
        else:
            agendamento = agendamento.objects.all()
            serializer = AgendamentoSerializer(agendamento, many=True)
            return Response({"Sucesso": serializer.data}, status=status.HTTP_200_OK)

    if request.method == "POST":
        serializer = AgendamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Sucesso": "Serviço criado"}, status=status.HTTP_201_CREATED)
        return Response({"ERRO": serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        
