from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .models import Servico, Salao
from .forms import ServicoForm
from django.contrib.auth.decorators import login_required

def servico_list(request, salao_id):
    if request.GET:
        filtro = {} #dicionário 
        for key, val in request.GET.lists():
            filtro.update({key + "__contains": val[0]})
        produtos = Servico.objects.all().filter(salao=salao_id, **filtro)
    else:
        produtos = Servico.objects.filter(salao=salao_id)
    return produtos
   
@login_required
def servico_add(request, id):
    salao = get_object_or_404(Salao, id=id)
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            servico = form.save(commit=False)
            servico.salao = salao
            servico.save()
            return redirect(reverse('salao_detail', args=[id]))
    else:
        form = ServicoForm()
    return render(request, "servico/servico_add.html", {'servico': form, 'salao': salao})

@login_required
def servico_delete(request, id):
    servico = get_object_or_404(Servico, id=id)
    salao_id = servico.salao.id
    servico.delete()
    return redirect(reverse('salao_detail', args=[salao_id]))

@login_required
def servico_edit(request, id):
    servico = get_object_or_404(Servico, id=id)
    salao = servico.salao
    
    if request.method == 'POST':
        form = ServicoForm(request.POST, instance=servico)
        if form.is_valid():
            form.save()
            salao_id = servico.salao.id
            return redirect(reverse('salao_detail', args=[salao_id]))
    else:
        form = ServicoForm(instance=servico)
    
    return render(request, "servico/servico_edit.html", {'servico': form, 'salao': salao})

def servico_detail(request, id):
    form = Servico.objects.all().filter(id=id)
    return render(request, 'servicos_template/index.html', {"servico": form})