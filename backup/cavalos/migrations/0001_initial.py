# Generated by Django 5.1.1 on 2024-09-18 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cavalos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frota', models.CharField(max_length=150, verbose_name='Frota')),
                ('placa', models.CharField(max_length=150, verbose_name='Placa')),
                ('motorista', models.CharField(max_length=150, verbose_name='Motorista padrão')),
                ('renavam', models.CharField(max_length=150, verbose_name='Renavam')),
                ('anomod', models.CharField(max_length=10, verbose_name='Ano / Modelo')),
                ('cor', models.CharField(max_length=20, verbose_name='Cor')),
                ('chassi', models.CharField(max_length=150, verbose_name='Chassi')),
                ('crlv', models.CharField(max_length=150, verbose_name='CRLV')),
                ('marca', models.CharField(max_length=20, verbose_name='Marca')),
                ('modelo', models.CharField(max_length=20, verbose_name='Modelo')),
                ('suspensao', models.CharField(max_length=20, verbose_name='Suspensão')),
                ('tracao', models.CharField(max_length=20, verbose_name='Tração')),
                ('altura', models.CharField(max_length=150, verbose_name='Altura')),
                ('capdiesel', models.CharField(max_length=150, verbose_name='Cap.Diesel')),
                ('pbt', models.CharField(max_length=20, verbose_name='PBT')),
                ('tara', models.CharField(max_length=20, verbose_name='Tara')),
                ('locado', models.CharField(max_length=20, verbose_name='Locado')),
                ('macaricoele', models.CharField(max_length=3, verbose_name='Maçarico eletrônico')),
                ('bombadeasfalto', models.CharField(max_length=3, verbose_name='Bomba de asfalto')),
                ('bombahidraulica', models.CharField(max_length=3, verbose_name='Bomba Hidráulica')),
                ('esperatforca', models.CharField(max_length=3, verbose_name='Espera T.Força')),
                ('placasolar', models.CharField(max_length=3, verbose_name='Placa solar')),
                ('status', models.CharField(max_length=20, verbose_name='Status')),
                ('bloqueador', models.CharField(max_length=20, verbose_name='Bloqueador')),
                ('transportadora', models.CharField(max_length=20, verbose_name='Transportadora')),
                ('notafiscal', models.CharField(max_length=3, verbose_name='Nota fiscal')),
                ('velocidade', models.CharField(max_length=20, verbose_name='Velocidade')),
                ('fimdegarantia', models.CharField(max_length=150, verbose_name='Fim De Garantia')),
                ('dataentregatecnica', models.CharField(max_length=150, verbose_name='Data Entrega Técnica')),
            ],
        ),
    ]
