from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status, response

from trading_network.models import TradingNetwork
from trading_network.serializers import TradingNetworkListSerializer, TradingNetworkSerializer


class TradingNetworkCreateAPIView(generics.CreateAPIView):
    """
    Класс для добавления звена сети.
    """

    serializer_class = TradingNetworkSerializer
    queryset = TradingNetwork.objects.all()

    def create(self, request, *args, **kwargs):
        """
        Метод проверяет на превышение вложенности сети и сохраняет объект сети.
        """
        if 'parent' in request.data:

            parent = TradingNetwork.objects.get(pk=request.data.get('parent'))

            if parent.level >= 2:
                return response.Response({'error': 'Структура сети может состоять максимум из 3х уровней!'},
                                         status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)


class TradingNetworkUpdateAPIView(generics.UpdateAPIView):
    """
    Класс для обновления звена сети.
    """

    serializer_class = TradingNetworkSerializer
    queryset = TradingNetwork.objects.all()

    def update(self, request, *args, **kwargs):
        """
        Метод запрещает изменять поле задолженность перед поставщиком и проверяет на превышение вложенности сети
        и сохраняет объект сети.
        """
        if 'debt' in request.data:
            return response.Response({'error': 'Запрет на изменение поля задолженность'},
                                     status=status.HTTP_400_BAD_REQUEST)

        if 'parent' in request.data:
            parent = TradingNetwork.objects.get(pk=request.data.get('parent'))

            if parent.level >= 2:
                return response.Response({'error': 'Структура сети может состоять максимум из 3х уровней!'},
                                         status=status.HTTP_400_BAD_REQUEST)
        return super().update(request, *args, **kwargs)


class TradingNetworkListAPIView(generics.ListAPIView):
    """
    Класс для просмотра списка торговых сетей.
    """

    serializer_class = TradingNetworkListSerializer
    queryset = TradingNetwork.objects.viewable()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('country',)


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
