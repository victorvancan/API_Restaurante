from  rest_framework import serializers
from django.db.models import Avg
from .models import Cardapio, Avalicacao


class CardapioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cardapio
        fields = (
            'id',
            'prato',
            'descricao',
            'url',
            'popularidade',
            'evento',
            'preco'
        )

    def get_media_popularidade(self, obj):
        media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao_avg')

        if media is None:
            return 0
        return round(media * 2)/ 2


class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avalicacao
        fields = (
            'id',
            'prato',
            'nome',
            'email',
            'comentario',
            'criticas',
            'satisfacao',
            'avaliacao',
            'evento'
        )

        def validate_avaliacao(self, valor):
            if valor in range(1, 6):
                return valor
            raise serializers.ValidationError('A avaliação precisa ser de 1 á 5')