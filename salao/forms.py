from django import forms
from .models import Salao

class SalaoForm(forms.ModelForm):
  class Meta:
    model = Salao
    fields = ['url_image', 'nome', 'endereco', 'descricao', 'CNPJ', 'telefone']
    exclude = ['proprietario']
    labels = {
      'url_image': 'Imagem do salão',
      'nome': 'Nome',
      'endereco': 'Endereço',
      'descricao': 'Descrição',
      'CNPJ': 'CNPJ',
      'telefone': 'Telefone'
    }
    widgets = {
      'url_image': forms.ClearableFileInput(attrs={
        'class': 'multisteps-form__input form-control',
        'accept': 'image/*'
      }),
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
