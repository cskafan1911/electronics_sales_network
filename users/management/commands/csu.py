import os

from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """
    Создание суперпользователя.
    """

    def handle(self, *args, **options):
        user = User.objects.create(
            username=os.getenv('ADMIN_USERNAME'),
            is_superuser=True,
            is_staff=True,
            is_active=True,
        )

        user.set_password(os.getenv('ADMIN_PASSWORD'))
        user.save()
