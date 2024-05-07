from rest_framework import generics

from trading_network.models import TradingNetwork
from trading_network.serializers import TradingNetworkListSerializer, TradingNetworkSerializer


class TradingNetworkCreateAPIView(generics.CreateAPIView):
    """
    Класс для добавления звена сети.
    """

    serializer_class = TradingNetworkSerializer

    def perform_create(self, serializer):
        """
        Метод для ограничения количества уровней вложенности (максимум 3 уровня).
        """
        link_of_network = serializer.save()
        if link_of_network.parent.level == 2:
            link_of_network.delete()
            raise ValueError('Структура сети может состоять максимум из 3х уровней!')


class TradingNetworkUpdateAPIView(generics.UpdateAPIView):
    """
    Класс для обновления звена сети.
    """

    serializer_class = TradingNetworkSerializer
    queryset = TradingNetwork.objects.all()


class TradingNetworkListAPIView(generics.ListAPIView):
    """
    Класс для просмотра списка торговых сетей.
    """

    serializer_class = TradingNetworkListSerializer
    queryset = TradingNetwork.objects.viewable()


class TradingNetworkDetailAPIView(generics.RetrieveAPIView):
    """
    Класс для просмотра торговой сети и его вложенных объектов.
    """

    serializer_class = TradingNetworkListSerializer

    def get_queryset(self, **kwargs):
        """
        Метод получает объект сети и все его вложенные объекты.
        """

        level_id = TradingNetwork.objects.get(pk=self.kwargs.get('pk')).level
        queryset = TradingNetwork.objects.viewable(level_id)
        return queryset


class TradingNetworkDeleteAPIView(generics.DestroyAPIView):
    """
    Класс для удаления объекта торговой сети.
    """

    queryset = TradingNetwork.objects.all()
    serializer_class = TradingNetworkSerializer
