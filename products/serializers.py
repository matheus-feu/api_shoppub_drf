from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Product.

    Este serializer é responsável por converter os dados do modelo Product em um formato que pode ser facilmente renderizado em uma resposta HTTP. Ele exclui os campos 'created_at', 'updated_at' e 'deleted_at' da serialização.
    """

    class Meta:
        model = Product
        exclude: tuple = ('created_at', 'updated_at', 'deleted_at')


class ProductUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer para atualização do modelo Product.

    Este serializer é responsável por converter os dados do modelo Product em um formato que pode ser facilmente renderizado em uma resposta HTTP. Ele inclui apenas os campos 'id' e 'deleted_at' na serialização, que são os campos relevantes para a operação de atualização.
    """

    class Meta:
        model = Product
        fields: list[str] = ['id', 'deleted_at']
