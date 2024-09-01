from django.shortcuts import redirect, render
from .forms import SalaoForm
from .models import Salao

# Create your views here.
def salao_list(request):
  saloes = Salao.objects.all()
  return render(request,'salao/salao_list.html', {'saloes': saloes})

def salao_detail(request, id):
  salao = Salao.objects.get(id=id)
  return render(request, 'salao/salao_detail.html', {'salao': salao})

def salao_add(request):
  if request.method == 'POST':
    form = SalaoForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('salao_list')
  else:
    form = SalaoForm()
  return render(request, 'salao/salao_form.html', {'form': form})

def salao_edit(request, id):
  salao = Salao.objects.get(id=id)
  if request.method == 'POST':
    form = SalaoForm(request.POST, instance=salao)
    if form.is_valid():
      form.save()
      return redirect('salao_list')
  else:
    form = SalaoForm(instance=salao)
  return render(request, 'salao/salao_form.html', {'form': form})

def salao_delete(request, id):
  salao = Salao.objects.get(id=id)
  salao.delete()
  return redirect('salao_list')