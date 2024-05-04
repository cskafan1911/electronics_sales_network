from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserManager(BaseUserManager):
    """
    Класс для настроек модели пользователь.
    """

    def create_user(self, username, password=None):
        """
        Метод сохраняет пароль пользователя в зашифрованном виде.
        """
        user = self.model(
            username=username
        )

        user.set_password(password)
        user.save(using=self._db)

        return user


class User(AbstractUser):
    """
    Класс для модели Пользователя.
    """

    username = models.CharField(max_length=50, unique=True, verbose_name='Имя для входа')
    first_name = models.CharField(max_length=150, verbose_name='Имя пользователя', blank=True, null=True)
    last_name = models.CharField(max_length=150, verbose_name='Фамилия пользователя', blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
