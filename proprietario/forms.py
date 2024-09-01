from django.contrib.auth.forms import UserCreationForm
from .models import Proprietario
from django.forms import EmailInput, PasswordInput, TextInput
class ProprietarioForm(UserCreationForm):
     class Meta:
        model = Proprietario
        fields = ['nome', 'email', 'telefone', 'especializacao', 'username']  # Definindo os campos específicos
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
            'especializacao': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Especialização',
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
        'especializacao': 'Especialização',
        'telefone': 'Telefone',
        'username': 'Nome de Usuário',
        'password1' : 'Senha',
        'password2' : 'Confirme a senha'
        }