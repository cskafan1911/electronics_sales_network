from rest_framework import serializers

from trading_network.models import TradingNetwork


class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class TradingNetworkSerializer(serializers.ModelSerializer):
    """
    Класс сериализатор для модели TradingNetwork.
    """

    class Meta:
        model = TradingNetwork
        fields = ('id', 'title', 'type_of_link', 'country', 'city', 'street', 'number_of_house', 'debt', 'parent',)


class TradingNetworkListSerializer(serializers.ModelSerializer):
    """
    Класс сериализатор для модели TradingNetwork.
    """

    children = RecursiveField(many=True)

    class Meta:
        model = TradingNetwork
        fields = ('id', 'title', 'type_of_link', 'country', 'city', 'street', 'number_of_house', 'debt', 'children',)
