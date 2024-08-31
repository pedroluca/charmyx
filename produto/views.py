from django.shortcuts import render, redirect
from .forms import ProdutoForm
from .models import Salao, Produto

# Create your views here.
def produto_list(request, salao_id):
  produtos = Produto.objects.all()
  return render(request, 'produto_list.html', {'salao_id': salao_id, 'produtos': produtos})

def produto_detail(request, salao_id, produto_id):
  produto = Produto.objects.get(id=produto_id)
  return render(request, 'produto_detail.html', {'salao_id': salao_id, 'produto': produto})

def produto_add(request, salao_id):
  if request.method == 'POST':
    form = ProdutoForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('produto_list', salao_id=salao_id)
  else:
    form = ProdutoForm()
  return render(request, 'produto_form.html', {'salao_id': salao_id, 'form': form})