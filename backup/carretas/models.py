from django.db import models


# Create your models here.

class Carretas(models.Model):
    frota = models.CharField(max_length=150, verbose_name="Frota")
    placa = models.CharField(max_length=150, unique=True, verbose_name="Placa")
    motorista = models.CharField(max_length=250, verbose_name="Motorista padrão")
    renavam = models.CharField(max_length=250, verbose_name="Renavam")

    GENDER_CHOICES = (
        ('A', '2024/2024'),
        ('B', '2023/2024'),
        ('C', '2022/2023'),
        ('D', '2021/2022'),
        ('E', '2020/2021'),
        ('F', '2019/2020'),
        ('G', '2018/2019'),
        ('H', '2017/2018'),
        ('I', '2016/2017'),
        ('J', '2015/2016'),
        ('K', '2014/2015'),
        ('L', '2013/2014'),
        ('M', '2012/2013'),
        ('N', '2011/2012'),
        ('O', '2010/2011'),
        ('P', '2009/2010'),
        ('Q', '2008/2009'),
        ('R', '2007/2008'),
        ('S', '2006/2007'),
        ('T', '2005/2006'),
        ('U', '2004/2005'),
    )
    anomod = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Ano / Modelo")

    GENDER_CHOICES = (
        ('A', 'Amarela'),
        ('B', 'Azul'),
        ('C', 'Branca'),
        ('D', 'Cinza'),
        ('E', 'Prata'),
        ('F', 'Preta'),
        ('G', 'Vermelho'),
    )
    cor = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Cor")
    chassi = models.CharField(max_length=150, verbose_name="Chassi")

    GENDER_CHOICES = (
        ('A', 'Araucária'),
    )
    crlv = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="CRLV")

    GENDER_CHOICES = (
        ('B', 'BIASI'),
        ('F', 'FACCHINI'),
        ('G', 'GOTTI'),
        ('K', 'KRONORTE'),
        ('M', 'METALESP'),
        ('R', 'R/TRIEL'),
        ('S', 'RANDON'),
        ('T', 'RECRUSUL'),
        ('U', 'RHODOSS'),
        ('V', 'RODOTEC'),
        ('W', 'RODOTÉCNICA'),
        ('X', 'RODOTIC'),
        ('Y', 'TRIEL'),
    )
    marca = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Marca")

    GENDER_CHOICES = (
        ('B', 'BITREM DIANTEIRO'),
        ('C', 'BITREM TRASEIRO'),
        ('D', 'QUATRO PATAS'),
        ('E', 'RODOTREM DIANTEIRO'),
        ('F', 'RODOTREM TRASEIRO'),
        ('G', 'VANDERLÉIA'),
    )
    modelo = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Modelo")

    GENDER_CHOICES = (
        ('A', '2'),
        ('B', '3'),
        ('C', '4'),
    )
    eixos = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Eixos")

    GENDER_CHOICES = (
        ('A', '295/80'),
        ('B', 'Single'),
    )
    pneus = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Pneus")

    GENDER_CHOICES = (
        ('M', 'Mecânica'),
        ('P', 'Pneumática'),
    )
    suspensao = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Suspensão")
    altura = models.DecimalField(max_digits=6, decimal_places=3, verbose_name="Altura")
    pbt = models.DecimalField(max_digits=6, decimal_places=3, verbose_name="PBT")
    toneladas = models.DecimalField(max_digits=6, decimal_places=3, verbose_name="Toneladas")
    litros = models.DecimalField(max_digits=6, decimal_places=3, verbose_name="Litros")

    GENDER_CHOICES = (
        ('A', 'A.CARB'),
        ('B', 'ALUM'),
        ('C', 'BASC'),
        ('D', 'INOX'),
        ('E', 'LS'),
        ('F', 'TERM'),
    )
    tipo = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Tipo")

    tara = models.DecimalField(max_digits=6, decimal_places=3, verbose_name="Tara")

    GENDER_CHOICES = (
        ('A', '1°'),
        ('B', '1°, 2°'),
        ('C', '1°, 2°, 3°'),
        ('D', '1°, 2°, 4°'),
        ('E', '1°, 3°'),
    )
    suspensor = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Suspensor eixos")
    bolsa = models.CharField(max_length=150, verbose_name="Bolsa suspensor")

    GENDER_CHOICES = (
        ('S', 'Sim'),
        ('N', 'Não'),
    )
    mola = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Mola pneumática")
    locada = models.CharField(max_length=150, verbose_name="Locada")

    GENDER_CHOICES = (
        ('V', 'VIA DUPLA'),
    )
    transportadora = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Transportadora")

    GENDER_CHOICES = (
        ('S', 'Sim'),
        ('N', 'Não'),
    )
    notafiscal = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Nota fiscal")
    status = models.CharField(max_length=150, verbose_name="Status")

    def __str__(self):
        return f"{self.placa}"


class Acessorios(models.Model):
    carreta = models.ForeignKey('Carretas', on_delete=models.CASCADE, related_name='Acessorios')
    placaacc = models.ForeignKey(Carretas, to_field='placa', on_delete=models.CASCADE, verbose_name="PlacaAcc")

    GENDER_CHOICES = (
        ('S', 'Sim'),
        ('N', 'Não'),
    )
    bottomclaro = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Bottom claro")

    GENDER_CHOICES = (
        ('S', 'Sim'),
        ('N', 'Não'),
    )
    bottomescuro = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Bottom escuro")

    GENDER_CHOICES = (
        ('S', 'Sim'),
        ('N', 'Não'),
    )
    bottomtepar = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Bottom Tepar")

    GENDER_CHOICES = (
        ('S', 'Sim'),
        ('N', 'Não'),
    )
    api = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="API")

    GENDER_CHOICES = (
        ('A', '1T'),
        ('B', '2T'),
        ('C', '2T ISOLADO'),
        ('D', 'Não'),
    )
    descarga = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Enc. Descarga")

    GENDER_CHOICES = (
        ('S', 'Sim'),
        ('N', 'Não'),
    )
    dreno = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Reg. No dreno")

    GENDER_CHOICES = (
        ('S', 'Sim'),
        ('N', 'Não'),
    )
    graudbolt = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Graud bolt Itajaí")

    GENDER_CHOICES = (
        ('S', 'Sim'),
        ('N', 'Não'),
    )
    olhodegato = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Olho de gato")

    GENDER_CHOICES = (
        ('S', 'Sim'),
        ('N', 'Não'),
    )
    mangote = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Mangote")

    GENDER_CHOICES = (
        ('S', 'Sim'),
        ('N', 'Não'),
    )
    macarico = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Maçarico")

    def __str__(self):
        return f"{self.placaacc.placa}"
