from rest_framework import serializers
from .models import Compra,Cliente

class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model=Compra
        fields='__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cliente
        fields='__all__'        