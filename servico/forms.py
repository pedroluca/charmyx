from django.forms import ModelForm, TextInput, TimeInput, NumberInput
from servico.models import Servico


class ServicoForm(ModelForm):
    class Meta:
        model = Servico
        fields = ['nome', 'descricao', 'valor', 'duracao']

        widgets = {
            'nome': TextInput(attrs={
                'class': 'multisteps-form__input form-control',
                'placeholder': 'Nome do serviço'
            }),
            'descricao': TextInput(attrs={
                'class': 'multisteps-form__input form-control',
                'placeholder': 'Descrição do serviço'
            }),
            'valor': NumberInput(attrs={
                'class': 'multisteps-form__input form-control',
                'placeholder': 'Valor do serviço',
                'step': '1.0' 
            }),
            'duracao': TimeInput(attrs={
                'class': 'multisteps-form__input form-control',
                'placeholder': 'Duração do serviço',
                'type': 'time'
            }),
        }
    