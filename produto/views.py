from django.shortcuts import render, redirect
from .forms import ProdutoForm
from .models import Produto
from salao.models import Salao

# Create your views here.
def produto_list(request, salao_id):
  produtos = Produto.objects.filter(salao=salao_id)
  return produtos

def produto_detail(request, salao_id, produto_id):
  produto = Produto.objects.get(pk=produto_id)
  salao = Salao.objects.get(pk=salao_id)
  return render(request, 'produto/produto_detail.html', {'salao_id': salao_id, 'produto': produto, 'salao': salao})

def produto_add(request, salao_id):
  if request.method == 'POST':
    form = ProdutoForm(request.POST)
    if form.is_valid():
      instance = form.save(commit=False)
      instance.salao = request.user.salao_id
      instance.save()
      return redirect('produto_list', salao_id=salao_id)
  else:
    form = ProdutoForm()
  return render(request, 'produto/produto_form.html', {'salao_id': salao_id, 'form': form})

def produto_edit(request, salao_id, produto_id):
  produto = Produto.objects.get(id=produto_id)
  if request.method == 'POST':
    form = ProdutoForm(request.POST, instance=produto)
    if form.is_valid():
      form.save()
      return redirect('produto_list', salao_id=salao_id)
  else:
    form = ProdutoForm(instance=produto)
  return render(request, 'produto/produto_form.html', {'salao_id': salao_id, 'form': form})

def produto_delete(request, salao_id, produto_id):
  produto = Produto.objects.get(id=produto_id)
  produto.delete()
  return redirect('produto_list', salao_id=salao_id)