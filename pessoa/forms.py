from django.contrib.auth.forms import UserCreationForm
from .models import Pessoa

class UserForm(UserCreationForm):
     class Meta:
        model = Pessoa
        fields = 'all'