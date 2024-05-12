from django.urls import path

from trading_network.apps import TradingNetworkConfig
from trading_network.views import TradingNetworkCreateAPIView, TradingNetworkListAPIView, TradingNetworkUpdateAPIView, \
    TradingNetworkDetailAPIView, TradingNetworkDeleteAPIView

app_name = TradingNetworkConfig.name

urlpatterns = [
    path('create/', TradingNetworkCreateAPIView.as_view(), name='trading_network_create'),
    path('info/<int:pk>/', TradingNetworkDetailAPIView.as_view(), name='trading_network_list'),
    path('', TradingNetworkListAPIView.as_view(), name='trading_network_list'),
    path('update/<int:pk>/', TradingNetworkUpdateAPIView.as_view(), name='trading_network_update'),
    path('delete/<int:pk>/', TradingNetworkDeleteAPIView.as_view(), name='trading_network_delete'),

]
