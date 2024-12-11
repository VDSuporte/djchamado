from django.db import models
from django.utils import timezone

class Justificativa(models.Model):
    nome = models.CharField(max_length=150, verbose_name="Nome")
    email = models.EmailField(max_length=254, verbose_name="E-mail")
    titulo = models.CharField(max_length=150, verbose_name="Título")
    descricao = models.TextField(max_length=500, verbose_name="Descrição")
    status = models.CharField(max_length=150, verbose_name="Status", default="Pendente")
    data = models.DateTimeField(verbose_name="Data/Hora", default=timezone.now)

    def __str__(self):
        return f"{self.nome}"
