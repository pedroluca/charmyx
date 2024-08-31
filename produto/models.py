from django.db import models

# Create your models here.
class Produto(models.Model):
  nome = models.CharField(max_length=100)
  preco = models.DecimalField(max_digits=10, decimal_places=2)
  descricao = models.TextField()
  quantidade_estoque = models.IntegerField()
  url_image = models.CharField(max_length=250)
  salao = models.ForeignKey('salao.Salao', on_delete=models.CASCADE)