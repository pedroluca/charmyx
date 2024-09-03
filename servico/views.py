from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Servico, Salao
from .forms import ServicoForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test



def servico_list(request):
    if request.GET:
        filtro = {} #dicionário 
        for key, val in request.GET.lists():
            filtro.update({key + "__contains": val[0]})
        
        form = Servico.objects.all().filter(**filtro)
    else:
        form = Servico.objects.all()
        
    return render(request, "servico/servico_list.html", {'servicos' : form})
   


def servico_add(request, id):
    sala = get_object_or_404(Salao, id=id)
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            servico = form.save(commit=False)
            servico.salao = sala
            servico.save()
            return redirect(reverse('salao_detail', args=[id]))
    else:
        form = ServicoForm()
    return render(request, "servico/servico_add.html", {'servico': form})


def servico_delete(request, id):
    servico = get_object_or_404(Servico, id=id)
    salao_id = servico.salao.id
    servico.delete()
    return redirect(reverse('salao_detail', args=[salao_id]))




def servico_edit(request, id):
    servico = get_object_or_404(Servico, id=id)
    salao_id = servico.salao.id
    
    if request.method == 'POST':
        form = ServicoForm(request.POST, instance=servico)
        if form.is_valid():
            form.save()
            return redirect(reverse('salao_detail', args=[salao_id]))
    else:
        form = ServicoForm(instance=servico)
    
    return render(request, "servico/servico_edit.html", {'servico': form})


def servico_detail(request, id):
    form = Servico.objects.all().filter(id=id)
    return render(request, 'servicos_template/index.html', {"servico": form})

