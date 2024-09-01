from django.contrib.auth.forms import UserCreationForm
from .models import Cliente
from django.forms import EmailInput, PasswordInput, TextInput
class ClienteForm(UserCreationForm):
     class Meta:
        model = Cliente
        fields = ['nome', 'email', 'cpf', 'telefone', 'username', 'password1', 'password2']  # Definindo os campos específicos
        widgets = {
            'nome': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome',
                'required': 'required'
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
                'required': 'required'
            }),
            'cpf': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'CPF',
                'required': 'required'
            }),
            'telefone': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Telefone',
                'required': 'required'
            }),
            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome de Usuário',
                'required': 'required'
            }),
            'password1' : PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Senha',
                'required': 'required'
            }),
            'password2' : PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirme a Senha',
                'required': 'required'
            }),
        }
        labels = {
        'first_name': 'Nome',
        'email': 'Email',
        'cpf': 'CPF',
        'telefone': 'Telefone',
        'username': 'Nome de Usuário',
        'password1' : 'Senha',
        'password2' : 'Confirme a senha'
        }