from rest_framework import viewsets
from .serializers import ProdutosSerializers
from ..models import Produto

class ProdutosViewsets(viewsets.ModelViewSet):
    serializer_class = ProdutosSerializers
    queryset = Produto.objects.all()