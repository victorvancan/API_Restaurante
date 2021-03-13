from django.db import models

class Base(models.Model):
    evento = models.CharField(max_length=100)
    aitvo = models.BooleanField(default=True)
    popularidade = models.CharField(max_length=20)

    class Meta:
        abstract = True



class Cardapio(Base):
    prato = models.CharField(max_length=50)
    descricao = models.CharField(max_length=500)
    preco = models.DecimalField(max_digits=5, decimal_places=2, default=True)



    class Meta:
        verbose_name = 'Cardapio'
        verbose_name_plural = 'Cardapios'
        ordering = ['id']


    def __str__(self):
        return self.prato


class Avalicacao(Base):
    prato = models.ForeignKey(Cardapio, related_name='avaliacoes', on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    comentario = models.TextField(blank=True, default='')
    criticas = models.TextField(blank=True, default='')
    satisfacao = models.DecimalField(max_digits=2, decimal_places=1)
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        unique_together = ['email', 'prato']
        ordering = ['prato']

    def __str__(self):
        return f'{self.nome} avaliou o prato {self.prato} com a nota {self.avalicao}'
