from django.contrib import admin
from .models import Agendamento, Servico
# Register your models here.
admin.site.register(Servico)
admin.site.register(Agendamento)