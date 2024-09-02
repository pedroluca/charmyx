from django.forms import ModelForm, TextInput
from servico.models import Servico


class ServicoForm(ModelForm):
    class Meta:
        model = Servico
        fields = ['nome', 'descricao', 'valor', 'duracao', 'salao_id']

        Widgets = {
            'nome': TextInput(attrs={
                'class': 'form-control form-control-user',
                'placeholder': 'Nome do serviço'
            }),
            'descricao': TextInput(attrs={
                'class': 'form-control form-control-user',
                'placeholder': 'Descrição do serviço'
            }),
            'valor': TextInput(attrs={
                'class': 'form-control form-control-user',
                'placeholder': 'Valor do serviço'
            }),
            'duracao': TextInput(attrs={
                'class': 'form-control form-control-user',
                'placeholder': 'Duração do serviço'
            }),
            'salao_id': TextInput(attrs={
                'class': 'form-control form-control-user',
                'placeholder': 'Salão do serviço'
            }),
        }