from django import forms
from agendamento.models import Agendamento
from datetime import time, timedelta
from django import forms
from agendamento.models import Agendamento
from datetime import time, timedelta

from servico.models import Servico

class AgendamentoForm(forms.ModelForm):
    # Defina os intervalos de tempo
    HORARIOS_MANHA = [(time(hour=h, minute=m).strftime('%H:%M'), f'{h:02}:{m:02}') for h in range(7, 12) for m in [0, 10, 20, 30, 40, 50]]
    HORARIOS_TARDE = [(time(hour=h, minute=m).strftime('%H:%M'), f'{h:02}:{m:02}') for h in range(14, 18) for m in [0, 10, 20, 30, 40, 50]]
    
    # Combine os intervalos de manhã e tarde
    HORARIOS_DISPONIVEIS = HORARIOS_MANHA + HORARIOS_TARDE
    horario = forms.ChoiceField(
        choices=HORARIOS_DISPONIVEIS,
        widget=forms.Select(attrs={
            'class': 'form-control form-control-user',
            'placeholder': 'Horário do agendamento'
        })
    )

    class Meta:
        model = Agendamento
        fields = ['horario', 'data', 'observacao', 'servico_id']

        widgets = {
            'data': forms.DateInput(attrs={
                'class': 'form-control form-control-user',
                'placeholder': 'Data do agendamento',
                'type': 'date'
            }),
            'observacao': forms.TextInput(attrs={
                'class': 'form-control form-control-user',
                'placeholder': 'Observação do agendamento'
            }),
            'servico_id': forms.Select(attrs={
                'class': 'form-control form-control-user',
                'placeholder': 'Serviço'
            })
        }
