from rest_framework import serializers 
from ..models import Cliente,Produto,Venda 

 
class ClienteSerializers(serializers.ModelSerializer):
    class Meta: 
       model = Cliente
       fields = "__all__" 

class ProdutoSerializers(serializers.ModelSerializer):
    class Meta: 
       model = Produto
       fields = "__all__" 

class VendaSerializers(serializers.ModelSerializer):
    class Meta: 
       model = Venda
       fields = "__all__" 