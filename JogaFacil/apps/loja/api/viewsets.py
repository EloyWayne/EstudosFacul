from rest_framework import viewsets 
from .serializers import ClienteSerializers,ProdutoSerializers,VendaSerializers
from ..models import Cliente,Produto,Venda

class ClienteViewsets(viewsets.ModelViewSet): 
  serializer_class = ClienteSerializers
  queryset = Cliente.objects.all()

class ProdutoViewsets(viewsets.ModelViewSet): 
  serializer_class =ProdutoSerializers
  queryset = Produto.objects.all()

class VendaViewsets(viewsets.ModelViewSet): 
  serializer_class = VendaSerializers
  queryset = Venda.objects.all()
