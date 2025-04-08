from django.db import models
from datetime import datetime
# Create your models here.

class Medico(models.Model):

    escolhas = [
        ("CAR","CAR"),
        ("GERAL", "GERAL"),
        ("PEDiATRA", "PEDIATRA")
    ]


    nome = models.CharField(max_length=255)
    especialidade = models.CharField(choices=escolhas, max_length=10)
    crm = models.CharField(max_length=8, unique=True)
    email = models.CharField(max_length=50, blank=True, null=True)

    
    def save(self, *args, **kwargs):
        if self.crm[2] == "/" and len(self.nome) >= 8:
            return super().save(*args, **kwargs)

  
    def __str__(self):
        return self.nome


class Client(models.Model):

    escolha = [
        ('agendado', 'agendado'),
        ('realizado','realizado'),
        ('cancelado', 'cancelado')
    ]

    paciente = models.CharField(max_length=50)
    data = models.DateField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    status = models.CharField(choices=escolha,max_length=10)


    def __str__(self):
        return self.paciente

    def save(self, *args, **kwargs):

        data_atual = datetime.now()
        validate_data = self.data >= data_atual

        if validate_data:
            return super().save(*args, **kwargs)