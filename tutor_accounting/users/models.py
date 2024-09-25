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
    cost = models.IntegerField(
        default=1000,
        verbose_name="Стоимость часа"
    )
    balance = models.IntegerField(
        default=0,
        verbose_name="Баланс"
    )
    is_student = models.BooleanField(
        default=False,
        verbose_name="Ученик"
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username


class Schedule(models.Model):
    choises = (
        ("Не выбрано", "Не выбрано"),
        ("Понедельник", "Понедельник"),
        ("Вторник", "Вторник"),
        ("Среда", "Среда"),
        ("Четверг", "Четверг"),
        ("Пятница", "Пятница"),
        ("Суббота", "Суббота"),
        ("Воскресенье", "Воскресенье")
    )
    student = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="schedule",
        verbose_name="Ученик"
    )
    weekday = models.CharField(
        max_length=50,
        default="Не выбрано",
        choices=choises,
        verbose_name="День недели",
    )
    time = models.TimeField(
        verbose_name="Время начала занятия"
    )

    class Meta:
        verbose_name = "День занятия"
        verbose_name_plural = "Дни занятий"

    def __str__(self):
        return f"{self.student} {self.weekday}"
