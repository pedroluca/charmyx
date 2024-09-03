from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import AgendamentoForm
from .models import Agendamento, Cliente

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test



def agendamento_list(request):
    if request.GET:
        filtro = {} #dicionário 
        for key, val in request.GET.lists():
            filtro.update({key + "__contains": val[0]})
        
        form = Agendamento.objects.all().filter(**filtro)
    else:
        form = Agendamento.objects.all()
        
    return render(request, "agendamento/index.html", {'agendamento' : form})
   

def agendamento_add(request):
    cliente = get_object_or_404(Cliente, id=request.user.id)

    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            agendamento = form.save(commit=False)
            agendamento.cliente_id = cliente 
            agendamento.save()
            salao_id = agendamento.servico_id.salao.id  # Acessa o salão através do serviço relacionado
            return redirect(reverse('salao_detail', args=[salao_id]))
    else:
        form = AgendamentoForm()

    return render(request, "agendamento/agendamento_add.html", {'agendamento': form})

def agendamento_delete(request, id):
    agendamento = get_object_or_404(Agendamento, id=id)
    salao_id = agendamento.servico_id.salao.id  # Acessa o salão através do serviço relacionado
    agendamento.delete()
    return redirect(reverse('salao_detail', args=[salao_id]))



def agendamento_edit(request, id):
    agendamento = Agendamento.objects.get(id=id)
    salao_id = agendamento.servico_id.salao.id  # Acessa o salão at 
    if request.method == 'POST':
        form = AgendamentoForm(request.POST, instance=agendamento)
        if form.is_valid():
            form.save()
            return redirect(reverse('salao_detail', args=[salao_id])) # R
    else:
        form = AgendamentoForm(instance=agendamento)

    return render(request, "agendamento/edit.html", {'agendamento': form})


def agendamento_detail(request, id):
    form = Agendamento.objects.all().filter(id=id)
    return render(request, 'agendamentos_template/index.html', {"agendamento": form})


def agendamento_confirm(request, id):
    agendamento = get_object_or_404(Agendamento, id=id)
    salao_id = agendamento.servico_id.salao.id  # Acessa o salão at
    agendamento.status = 'CON'
    agendamento.save()
    return redirect(reverse('salao_detail', args=[salao_id])) # Redireciona para a página de detalhes do salão

def agendamento_complete(request, id):
    agendamento = get_object_or_404(Agendamento, id=id)
    salao_id = agendamento.servico_id.salao.id  # Acessa o salão at
    agendamento.status = 'FIN'
    agendamento.save()
    return redirect(reverse('salao_detail', args=[salao_id])) # R