from rest_framework import serializers
from ..models import Produto

#forma 1 
class ProdutosSerializers(serializers.ModelSerializer):
    class Meta :
        model = Produto
        fields = "__all__"