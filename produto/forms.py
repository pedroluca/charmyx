from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'descricao', 'quantidade_estoque', 'url_image']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control form-control-user',
                'placeholder': 'Nome do produto'
            }),
            'preco': forms.TextInput(attrs={
                'class': 'form-control form-control-user',
                'placeholder': 'Preço do produto'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control form-control-user',
                'placeholder': 'Descrição do produto'
            }),
            'quantidade_estoque': forms.NumberInput(attrs={
                'class': 'form-control form-control-user',
                'placeholder': 'Quantidade em estoque'
            }),
            'url_image': forms.TextInput(attrs={
                'class': 'form-control form-control-user',
                'placeholder': 'URL da imagem do produto'
            }),
        }