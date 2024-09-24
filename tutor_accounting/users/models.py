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


class Payment(models.Model):
    student = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name="Ученик"
    )
    date = models.DateField(
        verbose_name="Месяц и год оплаты"
    )
    amount = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Оплата"
        verbose_name_plural = "Оплаты"

    def __str__(self):
        return f"Оплата {self.student} за {self.date}"
