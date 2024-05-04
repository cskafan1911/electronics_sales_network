from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Класс для модели Пользователя.
    """

    username = models.CharField(max_length=50, unique=True, verbose_name='Имя для входа')
    first_name = models.CharField(max_length=150, verbose_name='Имя пользователя', blank=True, null=True)
    last_name = models.CharField(max_length=150, verbose_name='Фамилия пользователя', blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
