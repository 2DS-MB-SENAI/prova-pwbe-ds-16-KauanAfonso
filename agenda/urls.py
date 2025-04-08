from django.urls import path
from . import views

urlpatterns = [
    path("servicos/<int:pk>", views.lidar_servico),
    path("servicos/", views.lidar_servico),
    path("agendamento/<int:pk>", views.lidar_agendamento),
    path("agendamento/", views.lidar_agendamento),
]
