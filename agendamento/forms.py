from django import forms
from agendamento.models import Agendamento
from servico.models import Servico
from datetime import time

class AgendamentoForm(forms.ModelForm):
    # Defina os intervalos de tempo
    HORARIOS_MANHA = [(time(hour=h, minute=m).strftime('%H:%M'), f'{h:02}:{m:02}') for h in range(7, 12) for m in [0, 25, 50]]
    HORARIOS_TARDE = [(time(hour=h, minute=m).strftime('%H:%M'), f'{h:02}:{m:02}') for h in range(14, 19) for m in [0, 25, 50]]
    
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

    def __init__(self, *args, **kwargs):
        # Recebe o parâmetro salao no init
        salao = kwargs.pop('salao', None)
        super().__init__(*args, **kwargs)
        
        if salao:
            # Filtra os serviços de acordo com o salão fornecido
            self.fields['servico_id'].queryset = Servico.objects.filter(salao=salao).order_by('nome')
        else:
            # Caso não tenha um salão específico, pode deixar vazio ou exibir todos os serviços
            self.fields['servico_id'].queryset = Servico.objects.none()
