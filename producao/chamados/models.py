from django.db import models
from django.utils import timezone

class Chamados(models.Model):
    email = models.EmailField(max_length=254, verbose_name="E-mail")
    nome = models.CharField(max_length=150, verbose_name="Nome")

    GENDER_CHOICES = (
        ('B', 'DIREÇÃO'),
        ('C', 'TECNOLOGIA'),
        ('D', 'LOGISTICA'),
        ('E', 'FATURAMENTO'),
        ('F', 'MANUTENÇÃO'),
    )

    departamento = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Departamento")


    descricao = models.TextField(max_length=500, verbose_name="Descrição")
    GENDER_CHOICES = (
        ('M', 'Pendente'),
        ('P', 'Concluído'),
    )

    status = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Status", default='M')
    data = models.DateTimeField(verbose_name="Data/Hora", default=timezone.now, editable="false")
    anexo = models.FileField(upload_to='anexos/', blank=True, null=True, verbose_name="false")

    def __str__(self):
        return f"{self.nome}"
