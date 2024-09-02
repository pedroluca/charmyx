from django.forms import ModelForm, TextInput, DateInput, TimeInput
from agendamento.models import Agendamento

class AgendamentoForm(ModelForm):
    class Meta:
        model = Agendamento
        fields = ['horario', 'data', 'observacao', 'status', 'servico_id', 'cliente_id']

        widgets = {
            'horario': TimeInput(attrs={
                'class': 'form-control form-control-user',
                'placeholder': 'Horário do agendamento',
                'type': 'time'  # Define o campo como um input de tempo
            }),
            'data': DateInput(attrs={
                'class': 'form-control form-control-user',
                'placeholder': 'Data do agendamento',
                'type': 'date'  # Define o campo como um input de data
            }),
            'observacao': TextInput(attrs={
                'class': 'form-control form-control-user',
                'placeholder': 'Observação do agendamento'
            }),
            'status': TextInput(attrs={
                'class': 'form-control form-control-user',
                'placeholder': 'Status do agendamento'
            })
        }
