import uuid
from django.db import models

from stdimage.models import StdImageField


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Servico(Base):
    SIDE_CHOICES = (
        ('direita', 'Direita'),
        ('esquerda', 'Esquerda'),
    )
    servico = models.CharField('Serviço', max_length=50)
    descricao = models.TextField('Descrição', max_length=300)
    lado = models.CharField('Lado', max_length=8, choices=SIDE_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.servico


class Design(Base):
    SIDE_CHOICES = (
        ('primeiro', 'Slide 1'),
        ('segundo', 'Slide 2'),
    )
    servico = models.CharField('Serviço', max_length=50)
    descricao = models.TextField('Descrição', max_length=150)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 355, 'height': 345, 'crop': True}})
    slide = models.CharField('Slide', max_length=8, choices=SIDE_CHOICES)

    class Meta:
        verbose_name = 'Design'
        verbose_name_plural = 'Designs'

    def __str__(self):
        return self.servico


class Descricao(Base):
    titulo = models.CharField('Titulo', max_length=40)
    sub_titulo = models.CharField('Sub Titulo', max_length=50)
    descricao = models.TextField('Descrição', max_length=2000)

    class Meta:
        verbose_name = 'Descricao'
        verbose_name_plural = 'Descriçoes'

    def __str__(self):
        return self.titulo


class Media(Base):
    nome = models.CharField('Nome', max_length=30)
    texto = models.CharField('Texto', max_length=30)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 132, 'height': 132, 'crop': True}})

    class Meta:
        verbose_name = 'Media'
        verbose_name_plural = 'Medias'

    def __str__(self):
        return self.nome
