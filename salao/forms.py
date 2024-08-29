from django import forms
from salao.models import Salao

class SalaoForm(forms.Form):
  # Define your form fields here
  nome = forms.TextInput(max_length=100)
  endereco = forms.TextInput(max_length=200)
  descricao = forms.Textarea()
  CNPJ = forms.TextInput(max_length=14)
  telefone = forms.TextInput(max_length=15)

  class Meta:
    model = Salao
    widgets = {
      'nome' : forms.TextInput(attrs={
        'class': 'form-control form-control-user',
        'placeholder': 'Nome do salão'
      }),
      'endereco' : forms.TextInput(attrs={
        'class': 'form-control form-control-user',
        'placeholder': 'Endereço do salão'
      }),
      'descricao' : forms.Textarea(attrs={
        'class': 'form-control form-control-user',
        'placeholder': 'Descrição do salão'
      }),
      'CNPJ' : forms.TextInput(attrs={
        'class': 'form-control form-control-user',
        'placeholder': 'CNPJ do salão'
      }),
      'telefone' : forms.TextInput(attrs={
        'class': 'form-control form-control-user',
        'placeholder': 'Telefone do salão'
      }),
    }
