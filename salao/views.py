from django.shortcuts import redirect, render
from proprietario.models import Proprietario
from .forms import SalaoForm
from .models import Salao
from produto.views import produto_list
from django.contrib.auth.decorators import login_required, user_passes_test

def salao_list(request):
  saloes = Salao.objects.all()
  is_proprietario = request.user.groups.filter(name='Proprietarios').exists()
  return render(request,'salao/salao_list.html', {'saloes': saloes, 'is_proprietario': is_proprietario})

def salao_detail(request, salao_id):
  salao = Salao.objects.get(pk=salao_id)
  produtos = produto_list(request, salao_id)
  is_proprietario = request.user.pk == salao.proprietario.pk
  return render(request, 'salao/salao_detail.html', {'salao': salao, 'produtos': produtos, 'is_proprietario': is_proprietario})

@login_required
def salao_add(request):
  if request.method == 'POST':
    form = SalaoForm(request.POST, request.FILES)
    if form.is_valid():
      salao = form.save(commit=False)
      try:
        proprietario = Proprietario.objects.get(pk=request.user.pk)
        salao.proprietario = proprietario
        salao.url_image = request.FILES['url_image']
        salao.save()
      except:
        return redirect('salao_add')  # Redirect back to salao_add if proprietario not found
      return redirect('salao_list')
  else:
    form = SalaoForm()
  return render(request, 'salao/salao_add.html', {'form': form})

@login_required
def salao_edit(request, salao_id):
  salao = Salao.objects.get(pk=salao_id)
  if request.method == 'POST':
    form = SalaoForm(request.POST, instance=salao)
    if form.is_valid():
      form.save()
      return redirect('salao_list')
  else:
    form = SalaoForm(instance=salao)
  return render(request, 'salao/salao_edit.html', {'form': form, 'salao': salao})

@login_required
def salao_delete(request, salao_id):
  Salao.objects.get(pk=salao_id).delete()
  return redirect('salao_list')