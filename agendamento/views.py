from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import AgendamentoForm
from .models import Agendamento, Cliente
from salao.models import Salao
from servico.models import Servico


def agendamento_list(request, salao_id):
    salao = get_object_or_404(Salao, id=salao_id)
    proprietario = salao.proprietario

    if request.user.id == proprietario.id:
        if request.GET:
            filtro = {}
            for key, val in request.GET.lists():
                filtro.update({key + "__contains": val[0]})
            agendamentos = Agendamento.objects.filter(servico_id__salao=salao, **filtro)
        else:
            agendamentos = Agendamento.objects.filter(servico_id__salao=salao)
    else:
        if request.GET:
            filtro = {}
            for key, val in request.GET.lists():
                filtro.update({key + "__contains": val[0]})
            agendamentos = Agendamento.objects.filter(cliente_id=request.user, servico_id__salao=salao, **filtro)
        else:
            agendamentos = Agendamento.objects.filter(cliente_id=request.user, servico_id__salao=salao)

    return agendamentos

def agendamento_add(request, salao_id):
    cliente = get_object_or_404(Cliente, id=request.user.id)

    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            agendamento = form.save(commit=False)
            agendamento.cliente_id = cliente 
            agendamento.save()
            salao_id = agendamento.servico_id.salao.id
            return redirect(reverse('salao_detail', args=[salao_id]))
    else:
        form = AgendamentoForm()

    return render(request, "agendamento/agendamento_add.html", {'agendamento': form, 'salao_id':salao_id})

def agendamento_delete(request, id):
    agendamento = get_object_or_404(Agendamento, id=id)
    salao_id = agendamento.servico_id.salao.id
    agendamento.delete()
    return redirect(reverse('salao_detail', args=[salao_id]))

@login_required
def agendamento_edit(request, id):
    agendamento = Agendamento.objects.get(id=id)
    salao_id = agendamento.servico_id.salao.id
    if request.method == 'POST':
        form = AgendamentoForm(request.POST, instance=agendamento)
        if form.is_valid():
            form.save()
            return redirect(reverse('salao_detail', args=[salao_id]))
    else:
        form = AgendamentoForm(instance=agendamento)

    return render(request, "agendamento/agendamento_edit.html", {'agendamento': form, 'salao_id':salao_id})

@login_required
def agendamento_confirm(request, id):
    agendamento = get_object_or_404(Agendamento, id=id)
    salao_id = agendamento.servico_id.salao.id
    agendamento.status = 'CON'
    agendamento.save()
    return redirect(reverse('salao_detail', args=[salao_id]))

@login_required
def agendamento_complete(request, id):
    agendamento = get_object_or_404(Agendamento, id=id)
    salao_id = agendamento.servico_id.salao.id
    agendamento.status = 'FIN'
    agendamento.save()
    return redirect(reverse('salao_detail', args=[salao_id]))