import os

from django.core.management import BaseCommand

from trading_network.models import TradingNetwork, Product


class Command(BaseCommand):

    def handle(self, *args, **options):

        TradingNetwork.objects.all().delete()
        return os.system('python manage.py loaddata electronics_network.json')
