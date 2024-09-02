from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import ServicoForm
from .models import Servico

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
        
    return render(request, "servico_templates/index.html", {'servico' : form})
   

def servico_add(request):

    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/servico/list/')
    else:
        form = ServicoForm()

    return render(request, "servico_templates/add.html", {'servico': form})




def servico_delete(request, id):
    servico = Servico.objects.get(id=id)
    servico.delete()
    return HttpResponseRedirect('/servico/list/')




def servico_edit(request, id):
    servico = Servico.objects.get(id=id)
    if request.method == 'POST':
        form = ServicoForm(request.POST, instance=servico)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/servico/list')
    else:
        form = ServicoForm(instance=servico)

    return render(request, "servico_templates/edit.html", {'servico': form})


def servico_detail(request, id):
    form = Servico.objects.all().filter(id=id)
    return render(request, 'servicos_template/index.html', {"servico": form})

