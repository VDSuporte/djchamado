from django.db import models

# Create your models here.

class Cavalos(models.Model):
    frota = models.CharField(max_length=150, verbose_name="Frota")
    placa = models.CharField(max_length=150, verbose_name="Placa")
    motorista = models.CharField(max_length=150, verbose_name="Motorista padrão")
    renavam = models.CharField(max_length=150, verbose_name="Renavam")
    anomod = models.CharField(max_length=10, verbose_name="Ano / Modelo")  # Alterado para CharField
    cor = models.CharField(max_length=20, verbose_name="Cor")  # Alterado para CharField
    chassi = models.CharField(max_length=150, verbose_name="Chassi")
    crlv = models.CharField(max_length=150, verbose_name="CRLV")
    marca = models.CharField(max_length=20, verbose_name="Marca")  # Alterado para CharField
    modelo = models.CharField(max_length=20, verbose_name="Modelo")  # Alterado para CharField
    suspensao = models.CharField(max_length=20, verbose_name="Suspensão")  # Alterado para CharField
    tracao = models.CharField(max_length=20, verbose_name="Tração")  # Alterado para CharField
    altura = models.CharField(max_length=150, verbose_name="Altura")
    capdiesel = models.CharField(max_length=150, verbose_name="Cap.Diesel")
    pbt = models.CharField(max_length=20, verbose_name="PBT")
    tara = models.CharField(max_length=20, verbose_name="Tara")
    locado = models.CharField(max_length=20, verbose_name="Locado")  # Alterado para CharField
    macaricoele = models.CharField(max_length=3, verbose_name="Maçarico eletrônico")  # Alterado para CharField
    bombadeasfalto = models.CharField(max_length=3, verbose_name="Bomba de asfalto")  # Alterado para CharField
    bombahidraulica = models.CharField(max_length=3, verbose_name="Bomba Hidráulica")  # Alterado para CharField
    esperatforca = models.CharField(max_length=3, verbose_name="Espera T.Força")  # Alterado para CharField
    placasolar = models.CharField(max_length=3, verbose_name="Placa solar")  # Alterado para CharField
    status = models.CharField(max_length=20, verbose_name="Status")  # Alterado para CharField
    bloqueador = models.CharField(max_length=20, verbose_name="Bloqueador")  # Alterado para CharField
    transportadora = models.CharField(max_length=20, verbose_name="Transportadora")  # Alterado para CharField
    notafiscal = models.CharField(max_length=3, verbose_name="Nota fiscal")  # Alterado para CharField
    velocidade = models.CharField(max_length=20, verbose_name="Velocidade")  # Alterado para CharField
    fimdegarantia = models.CharField(max_length=150, verbose_name="Fim De Garantia")
    dataentregatecnica = models.CharField(max_length=150, verbose_name="Data Entrega Técnica")

    def __str__(self):
        return f"{self.placa} "