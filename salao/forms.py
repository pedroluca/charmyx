from django import forms
from .models import Salao

class SalaoForm(forms.ModelForm):
  class Meta:
    model = Salao
    fields = ['nome', 'endereco', 'descricao', 'CNPJ', 'telefone']
    labels = {
      'nome': 'Nome',
      'endereco': 'Endereço',
      'descricao': 'Descrição',
      'CNPJ': 'CNPJ',
      'telefone': 'Telefone'
    }
    widgets = {
      'nome' : forms.TextInput(attrs={
        'class': 'multisteps-form__input form-control',
        'placeholder': 'ex: Salão da Leila'
      }),
      'endereco' : forms.TextInput(attrs={
        'class': 'multisteps-form__input form-control',
        'placeholder': 'ex: Rua das Flores, 123, Bairro Ipanema'
      }),
      'descricao' : forms.Textarea(attrs={
        'class': 'multisteps-form__input form-control',
        'placeholder': 'Descrição'
      }),
      'CNPJ' : forms.TextInput(attrs={
        'class': 'multisteps-form__input form-control',
        'placeholder': 'xxx.xxx.xxx/xxxx-xx'
      }),
      'telefone' : forms.TextInput(attrs={
        'class': 'multisteps-form__input form-control',
        'placeholder': '(xx) xxxxx-xxxx'
      }),
    }
