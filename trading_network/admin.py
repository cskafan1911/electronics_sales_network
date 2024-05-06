from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from django_mptt_admin.admin import DjangoMpttAdmin

from trading_network.models import Product, TradingNetwork

admin.site.register(Product)


class TradingNetworkAdmin(DjangoMpttAdmin):
    """
    Класс для админки объекта Торговая сеть.
    """

    list_display = ('title', 'parent_link', 'city', 'debt',)
    list_display_links = ('title', 'parent_link',)
    list_filter = ('city',)

    @admin.display(description='Ссылка на поставщика')
    def parent_link(self, obj):
        """
        Метод для получения ссылки на объект поставщика.
        """
        if not obj.parent_id:
            return f'Поставщика нет'
        else:
            app_label = obj._meta.app_label
            model_label = obj._meta.model_name
            url = reverse(
                f'admin:{app_label}_{model_label}_change', args=(obj.parent_id,)
            )
            return mark_safe(f'<a href="{url}">{obj.parent.title}</a>')


admin.site.register(TradingNetwork, TradingNetworkAdmin)
