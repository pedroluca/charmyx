from django.shortcuts import render, redirect
from .forms import ProdutoForm
from .models import Produto
from salao.models import Salao
from django.contrib.auth.decorators import login_required

def produto_list(request, salao_id):
  produtos = Produto.objects.filter(salao=salao_id)
  return produtos

def produto_detail(request, salao_id, produto_id):
  produto = Produto.objects.get(pk=produto_id)
  salao = Salao.objects.get(pk=salao_id)
  is_proprietario = request.user.pk == salao.proprietario.pk
  return render(request, 'produto/produto_detail.html', {'salao_id': salao_id, 'produto': produto, 'salao': salao, 'is_proprietario': is_proprietario})

@login_required
def produto_add(request, salao_id):
  salao = Salao.objects.get(pk=salao_id)
  if request.method == 'POST':
    form = ProdutoForm(request.POST, request.FILES  )
    if form.is_valid():
      instance = form.save(commit=False)
      instance.salao = salao
      instance.url_image = request.FILES['url_image']
      instance.save()
      if request.POST.get('action') == 'save_add_another':
        return redirect('produto_add', salao_id=salao_id)
      else:
        return redirect('salao_detail', salao_id=salao_id)
    else:
      print(form.errors)
  else:
    form = ProdutoForm()
  return render(request, 'produto/produto_add.html', {'salao': salao, 'form': form})

@login_required
def produto_edit(request, salao_id, produto_id):
  produto = Produto.objects.get(id=produto_id)
  if request.method == 'POST':
    form = ProdutoForm(request.POST, instance=produto)
    if form.is_valid():
      form.save()
      return redirect('produto_detail', salao_id=salao_id, produto_id=produto_id)
  else:
    form = ProdutoForm(instance=produto)
  return render(request, 'produto/produto_edit.html', {'form': form, 'produto': produto, 'salao_id': salao_id})

@login_required
def produto_delete(request, salao_id, produto_id):
  Produto.objects.get(pk=produto_id).delete()
  return redirect('salao_detail', salao_id=salao_id)