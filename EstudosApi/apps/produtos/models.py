from django.db import models

class Produto(models.Model):
    TAMANHO_LISTA = [
        ('P','Small'),
        ('M','Medio'),
        ('L','Large')
    ]
    
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    descricao = models.CharField(max_length=150, null=True, blank=True)
    tamanho = models.CharField(max_length=2, choices=TAMANHO_LISTA, null=True, blank=True)

    def __str__(self):
        return self.nome
