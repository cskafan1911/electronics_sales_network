from django.db import models
from mptt.managers import TreeManager
from mptt.models import MPTTModel, TreeForeignKey


class Product(models.Model):
    """
    Класс для товара.
    """

    manufacturer = models.ForeignKey('TradingNetwork', on_delete=models.PROTECT, related_name='product',
                                     verbose_name='Производитель')
    title = models.CharField(max_length=100, verbose_name='Название товара')
    model = models.CharField(max_length=150, verbose_name='Модель товара')
    release_date = models.DateField(verbose_name='Дата выхода')

    def __str__(self):
        """
        Строковое представление объекта Product.
        """
        return f'{self.title} ({self.model})'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class TradingNetworkManager(TreeManager):

    def viewable(self, level=0):
        queryset = self.get_queryset().filter(level=level)
        return queryset


class TradingNetwork(MPTTModel):
    """
    Класс для торговой сети.
    """

    FACTORY = 'FACTORY'
    RETAIL = 'RETAIL'
    INDIVIDUAL_ENTREPRENEUR = 'INDIVIDUAL_ENTREPRENEUR'

    TYPE = [
        (FACTORY, 'Завод'),
        (RETAIL, 'Розничная сеть'),
        (INDIVIDUAL_ENTREPRENEUR, 'ИП'),
    ]

    title = models.CharField(max_length=100, verbose_name='Название')
    type_of_link = models.CharField(max_length=23, choices=TYPE)
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children',
                            db_index=True, verbose_name='Поставщик')
    debt = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='Задолженность')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    email = models.EmailField(unique=True, verbose_name='email', blank=True, null=True)
    country = models.CharField(max_length=50, verbose_name='Страна')
    city = models.CharField(max_length=50, verbose_name='Город')
    street = models.CharField(max_length=50, verbose_name='Улица')
    number_of_house = models.IntegerField(verbose_name='Номер дома')

    objects = TradingNetworkManager()

    def __str__(self):
        """
        Строковое представление модели TradingNetwork.
        """
        return f'{self.title} ({self.type_of_link})'

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
