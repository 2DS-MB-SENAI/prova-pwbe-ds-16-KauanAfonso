from django.shortcuts import render, get_object_or_404
from .models import *
from .form import FormConsulta
from django.http import HttpResponseNotFound
''''

### Views obrigatórias:
1. `listar_medicos` - Lista todos os médicos cadastrados
2. `criar_consulta` - Formulário para agendar nova consulta
3. `detalhes_consulta` - Exibe informações de uma consulta específica

'''
# Create your views here.

def listar_medicos(request):
    medicos = Medico.objects.all()
    return render(request, 'listar_medicos.html', {'medicos':medicos})


def listar_consulta(request, id):
    try:
        consultas = get_object_or_404(Client,pk=id)
    except:
        return HttpResponseNotFound("Não encontrado")
    
    return render(request, "", {'consultas': consultas})


def listar_medico_um(request, id):
    try:
        medicos = get_object_or_404(Medico,pk=id)
    except:
        return HttpResponseNotFound("Não encontrado")
    
    return render(request, "", {'medicos': medicos})


'''

func para criar consulta com base no formulario FormConsulta;
Realiza validações de dados corretos e se o form foi enviado.

'''
def criar_consulta(request):
    if request.method == "POST":
        consulta = request.POST
        form = FormConsulta(consulta)
        if form.is_valid():
            form.save()
            return render(request, 'form_consulta.html', {"msg":"Consulta marcada !"} )
        else:
            return render(request, 'form_consulta.html', {"msg":"Algo deu errado !"} )
    else:
        form = FormConsulta()
    return render(request, 'form_consulta.html', {"form":form} )
