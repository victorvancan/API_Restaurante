from django.contrib import admin
from .models import Cardapio, Avalicacao


@admin.register(Cardapio)
class CardapioAdmin(admin.ModelAdmin):
    list_display = ('prato', 'descricao', 'evento', 'popularidade', 'preco')


@admin.register(Avalicacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display =  ('prato', 'nome', 'email', 'avaliacao', 'comentario', 'criticas', 'satisfacao')
