from django.urls import path
from . import views

'''
- `/medicos/` → Listagem de médicos
- `/consultas/nova/` → Agendamento
- `/consultas/<int:id>/` → Detalhes da consulta


'''

urlpatterns = [
    path('medicos/', views.listar_medicos, name="ListarMedicos"),
    path('medicos/<int:id>/', views.listar_medico_um, name="Buscar medico"),
    path("consultas/nova/", views.criar_consulta, name="Criar_Consulta"),
    path("consultas/<int:id>/", views.listar_consulta, name="Listar_Consulta")
]
