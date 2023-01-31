# Generated by Django 4.1.5 on 2023-01-19 16:30

import core.models
from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Descricao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('titulo', models.CharField(max_length=40, verbose_name='Titulo')),
                ('sub_titulo', models.CharField(max_length=50, verbose_name='Sub Titulo')),
                ('descricao', models.TextField(max_length=2000, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Descricao',
                'verbose_name_plural': 'Descriçoes',
            },
        ),
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('servico', models.CharField(max_length=50, verbose_name='Serviço')),
                ('descricao', models.TextField(max_length=150, verbose_name='Descrição')),
                ('imagem', stdimage.models.StdImageField(force_min_size=False, upload_to=core.models.get_file_path, variations={'thumb': {'crop': True, 'height': 345, 'width': 355}}, verbose_name='Imagem')),
                ('slide', models.CharField(choices=[('1', 'Slide 1'), ('2', 'Slide 2')], max_length=1, verbose_name='Lado')),
            ],
            options={
                'verbose_name': 'Design',
                'verbose_name_plural': 'Designs',
            },
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('servico', models.CharField(max_length=50, verbose_name='Serviço')),
                ('descricao', models.TextField(max_length=300, verbose_name='Descrição')),
                ('lado', models.CharField(choices=[('direita', 'Direita'), ('esquerda', 'Esquerda')], max_length=8, verbose_name='Lado')),
            ],
            options={
                'verbose_name': 'Serviço',
                'verbose_name_plural': 'Serviços',
            },
        ),
    ]