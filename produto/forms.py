from django import forms
from .models import Produto, Salao

class ProdutoForm(forms.ModelForm):
  # Define your form fields here
  nome = forms.TextInput(max_length=100)
  preco = forms.DecimalField(max_digits=10, decimal_places=2)
  descricao = forms.Textarea()
  quantidade_estoque = forms.IntegerField()
  url_image = forms.TextInput(max_length=250)
  salao = forms.ModelChoiceField(queryset=Salao.objects.all())

  class Meta:
    model = Produto
    widgets = {
      'nome' : forms.TextInput(attrs={
        'class': 'form-control form-control-user',
        'placeholder': 'Nome do produto'
      }),
      'preco' : forms.TextInput(attrs={
        'class': 'form-control form-control-user',
        'placeholder': 'Preço do produto'
      }),
      'descricao' : forms.Textarea(attrs={
        'class': 'form-control form-control-user',
        'placeholder': 'Descrição do produto'
      }),
      'quantidade_estoque' : forms.TextInput(attrs={
        'class': 'form-control form-control-user',
        'placeholder': 'Quantidade em estoque'
      }),
      'url_image' : forms.TextInput(attrs={
        'class': 'form-control form-control-user',
        'placeholder': 'URL da imagem do produto'
      }),
      'salao' : forms.Select(attrs={
        'class': 'form-control form-control-user',
        'placeholder': 'Salão do produto'
      }),
    }