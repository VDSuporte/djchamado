from django.db import models
from django.utils.crypto import get_random_string
# Create your models here.

class Clientes(models.Model):
    codigo = models.CharField(max_length=150, verbose_name="Código")
    cliente = models.CharField(max_length=150, verbose_name="Cliente")
    cliente_fantasia = models.CharField(max_length=150, verbose_name="Nome fantasia")
    observacao = models.TextField(max_length=500, verbose_name="Observação")
    representante = models.CharField(max_length=150, verbose_name="Representante")
    contato = models.CharField(max_length=150, verbose_name="E-mail")
    def __str__(self):
        return f"{self.cliente} "
