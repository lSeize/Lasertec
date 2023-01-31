from django.contrib import admin

from .models import Design, Servico, Descricao, Media


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'descricao', 'lado', 'modificado')


@admin.register(Design)
class DesignAdmin(admin.ModelAdmin):
    list_display = ('servico', 'descricao', 'imagem', 'slide', 'modificado')


@admin.register(Descricao)
class DescricaoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'sub_titulo', 'descricao')


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'texto', 'imagem', 'modificado')
