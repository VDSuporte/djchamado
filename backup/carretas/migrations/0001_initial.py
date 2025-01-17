# Generated by Django 5.1.1 on 2024-09-18 13:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carretas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frota', models.CharField(max_length=150, verbose_name='Frota')),
                ('placa', models.CharField(max_length=150, unique=True, verbose_name='Placa')),
                ('motorista', models.CharField(max_length=250, verbose_name='Motorista padrão')),
                ('renavam', models.CharField(max_length=250, verbose_name='Renavam')),
                ('anomod', models.CharField(choices=[('A', '2024/2024'), ('B', '2023/2024'), ('C', '2022/2023'), ('D', '2021/2022'), ('E', '2020/2021'), ('F', '2019/2020'), ('G', '2018/2019'), ('H', '2017/2018'), ('I', '2016/2017'), ('J', '2015/2016'), ('K', '2014/2015'), ('L', '2013/2014'), ('M', '2012/2013'), ('N', '2011/2012'), ('O', '2010/2011'), ('P', '2009/2010'), ('Q', '2008/2009'), ('R', '2007/2008'), ('S', '2006/2007'), ('T', '2005/2006'), ('U', '2004/2005')], max_length=1, verbose_name='Ano / Modelo')),
                ('cor', models.CharField(choices=[('A', 'Amarela'), ('B', 'Azul'), ('C', 'Branca'), ('D', 'Cinza'), ('E', 'Prata'), ('F', 'Preta'), ('G', 'Vermelho')], max_length=1, verbose_name='Cor')),
                ('chassi', models.CharField(max_length=150, verbose_name='Chassi')),
                ('crlv', models.CharField(choices=[('A', 'Araucária')], max_length=1, verbose_name='CRLV')),
                ('marca', models.CharField(choices=[('B', 'BIASI'), ('F', 'FACCHINI'), ('G', 'GOTTI'), ('K', 'KRONORTE'), ('M', 'METALESP'), ('R', 'R/TRIEL'), ('S', 'RANDON'), ('T', 'RECRUSUL'), ('U', 'RHODOSS'), ('V', 'RODOTEC'), ('W', 'RODOTÉCNICA'), ('X', 'RODOTIC'), ('Y', 'TRIEL')], max_length=1, verbose_name='Marca')),
                ('modelo', models.CharField(choices=[('B', 'BITREM DIANTEIRO'), ('C', 'BITREM TRASEIRO'), ('D', 'QUATRO PATAS'), ('E', 'RODOTREM DIANTEIRO'), ('F', 'RODOTREM TRASEIRO'), ('G', 'VANDERLÉIA')], max_length=1, verbose_name='Modelo')),
                ('eixos', models.CharField(choices=[('A', '2'), ('B', '3'), ('C', '4')], max_length=1, verbose_name='Eixos')),
                ('pneus', models.CharField(choices=[('A', '295/80'), ('B', 'Single')], max_length=1, verbose_name='Pneus')),
                ('suspensao', models.CharField(choices=[('M', 'Mecânica'), ('P', 'Pneumática')], max_length=1, verbose_name='Suspensão')),
                ('altura', models.DecimalField(decimal_places=3, max_digits=6, verbose_name='Altura')),
                ('pbt', models.DecimalField(decimal_places=3, max_digits=6, verbose_name='PBT')),
                ('toneladas', models.DecimalField(decimal_places=3, max_digits=6, verbose_name='Toneladas')),
                ('litros', models.DecimalField(decimal_places=3, max_digits=6, verbose_name='Litros')),
                ('tipo', models.CharField(choices=[('A', 'A.CARB'), ('B', 'ALUM'), ('C', 'BASC'), ('D', 'INOX'), ('E', 'LS'), ('F', 'TERM')], max_length=1, verbose_name='Tipo')),
                ('tara', models.DecimalField(decimal_places=3, max_digits=6, verbose_name='Tara')),
                ('suspensor', models.CharField(choices=[('A', '1°'), ('B', '1°, 2°'), ('C', '1°, 2°, 3°'), ('D', '1°, 2°, 4°'), ('E', '1°, 3°')], max_length=1, verbose_name='Suspensor eixos')),
                ('bolsa', models.CharField(max_length=150, verbose_name='Bolsa suspensor')),
                ('mola', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=1, verbose_name='Mola pneumática')),
                ('locada', models.CharField(max_length=150, verbose_name='Locada')),
                ('transportadora', models.CharField(choices=[('V', 'VIA DUPLA')], max_length=1, verbose_name='Transportadora')),
                ('notafiscal', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=1, verbose_name='Nota fiscal')),
                ('status', models.CharField(max_length=150, verbose_name='Status')),
            ],
        ),
        migrations.CreateModel(
            name='Acessorios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bottomclaro', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=1, verbose_name='Bottom claro')),
                ('bottomescuro', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=1, verbose_name='Bottom escuro')),
                ('bottomtepar', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=1, verbose_name='Bottom Tepar')),
                ('api', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=1, verbose_name='API')),
                ('descarga', models.CharField(choices=[('A', '1T'), ('B', '2T'), ('C', '2T ISOLADO'), ('D', 'Não')], max_length=1, verbose_name='Enc. Descarga')),
                ('dreno', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=1, verbose_name='Reg. No dreno')),
                ('graudbolt', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=1, verbose_name='Graud bolt Itajaí')),
                ('olhodegato', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=1, verbose_name='Olho de gato')),
                ('mangote', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=1, verbose_name='Mangote')),
                ('macarico', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=1, verbose_name='Maçarico')),
                ('carreta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Acessorios', to='carretas.carretas')),
                ('placaacc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carretas.carretas', to_field='placa', verbose_name='PlacaAcc')),
            ],
        ),
    ]
