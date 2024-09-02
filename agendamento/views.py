from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import AgendamentoForm
from .models import Agendamento

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
        
    return render(request, "agendamento_templates/index.html", {'agendamento' : form})
   

def agendamento_add(request):

    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/agendamento/list/')
    else:
        form = AgendamentoForm()

    return render(request, "agendamento_templates/add.html", {'agendamento': form})




def agendamento_delete(request, id):
    agendamento = Agendamento.objects.get(id=id)
    agendamento.delete()
    return HttpResponseRedirect('/agendamento/list/')




def agendamento_edit(request, id):
    agendamento = Agendamento.objects.get(id=id)
    if request.method == 'POST':
        form = AgendamentoForm(request.POST, instance=agendamento)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/agendamento/list')
    else:
        form = AgendamentoForm(instance=agendamento)

    return render(request, "agendamento_templates/edit.html", {'agendamento': form})


def agendamento_detail(request, id):
    form = Agendamento.objects.all().filter(id=id)
    return render(request, 'agendamentos_template/index.html', {"agendamento": form})


