from django.db import models

class Cliente(models.Model):
    LISTA_GENERO = [
        ('M','Masculino'),
        ('F','Feminino'),
        ('N','Prefiro não informar')
    ]
    nome = models.CharField(max_length=50)
    sexo = models.CharField(max_length=2,choices=LISTA_GENERO)
    data_nacimento = models.DateField()
    endereco = models.TextField()

    def __str__(self):
        return self.nome

class Produto(models.Model):
    LISTA_TAMANHO = [
        ('P','Pequeno'),
        ('M','Medio'),
        ('G','Grande')
    ]
    nome = models.CharField(max_length=50)
    tamanho = models.CharField(max_length=2,choices=LISTA_TAMANHO)
    preco_custo = models.FloatField()
    preco_untario = models.FloatField()

    def __str__(self):
        return self.nome
    

class Venda(models.Model):
    LISTA_TIPO_DE_PAGAMENTO = [
        ('C','Cartão'),
        ('B','Boleto'),
        ('V','A Vista'),
        ('P','Pix'),
    ]

    LISTA_MEIO_DE_PAGAMENTO = [
        ('P','Presencial'),
        ('O','Online'),    
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    desconto = models.FloatField()
    tipo_pagamento =  models.CharField(max_length=2,choices=LISTA_TIPO_DE_PAGAMENTO)
    meio_de_pagamento = models.CharField(max_length=2,choices=LISTA_MEIO_DE_PAGAMENTO)

    def __str__(self):
        return self.cliente.nome +'/'+ self.produto.nome
