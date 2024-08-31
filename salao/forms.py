from django import forms
from .models import Salao

class SalaoForm(forms.ModelForm):
  # Define your form fields here
  nome = forms.CharField(max_length=100, required=True)
  endereco = forms.CharField(max_length=200, required=True)
  descricao = forms.CharField(widget=forms.Textarea)
  CNPJ = forms.CharField(max_length=14, required=True)
  telefone = forms.CharField(max_length=15, required=True)

  class Meta:
    model = Salao
    fields = '__all__'
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
