from django.urls import path
from . import views

urlpatterns = [
    path("servicos/<int:pk>", views.lidar_servico),
    path("servicos/", views.lidar_servico),
    path("agendamentos/<int:pk>", views.lidar_agendamento),
    path("agendamentos/", views.lidar_agendamento),
]
