from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Логин",
    )
    email = models.EmailField(
        max_length=50,
        unique=True,
        verbose_name="Почта",
    )
    first_name = models.CharField(
        max_length=50,
        verbose_name="Ваше имя",
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name="Ваша фамилия",
        blank=True,
        null=True,
    )
    cost = models.IntegerField(default=1000)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username
