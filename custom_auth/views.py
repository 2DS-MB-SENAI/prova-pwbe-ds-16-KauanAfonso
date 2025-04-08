from django.shortcuts import render
from . serializers import ServicoSerializer, AgendamentoSerializer
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.decorators import api_view
from .models import CustomUser
# Create your views here.


@api_view(['POST'])
def logar():
    pass