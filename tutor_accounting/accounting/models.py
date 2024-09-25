from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Student(models.Model):
    first_name = models.CharField(
        max_length=50,
        verbose_name="Имя",
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name="Фамилия",
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

    class Meta:
        verbose_name = "Ученик"
        verbose_name_plural = "Ученики"

    def __str__(self):
        return self.first_name


class Lesson(models.Model):
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Ученик"
    )
    tutor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="tutor",
        verbose_name="Преподаватель"
    )
    date = models.DateTimeField(
        verbose_name="Дата проведения занятия"
    )
    paid_for = models.BooleanField(
        default=False,
        verbose_name="Оплачено"
    )
    conducted = models.BooleanField(
        default=False,
        verbose_name="Проведено"
    )
    is_cancelled = models.BooleanField(
        default=False,
        verbose_name="Отменено"
    )

    class Meta:
        verbose_name = "Занятие"
        verbose_name_plural = "Занятия"

    def __str__(self):
        return f"Занятие {self.student} {self.date}"


class LessonAccounting(models.Model):
    month = models.CharField(
        max_length=50,
        verbose_name="Месяц"
    )
    year = models.CharField(
        max_length=50,
        verbose_name="Год"
    )
    quantity_conducted = models.IntegerField(
        default=0,
        verbose_name="Количество проведенных"
    )
    quantity_paid = models.IntegerField(
        default=0,
        verbose_name="Количество оплаченных"
    )
    quantity_cancelled = models.IntegerField(
        default=0,
        verbose_name="Количество отменённых"
    )
    quantity_moved = models.IntegerField(
        default=0,
        verbose_name="Количество перенесённых"
    )

    class Meta:
        verbose_name = "Учёт занятий"
        verbose_name_plural = "Учёты занятий"


class Payment(models.Model):
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Ученик"
    )
    date = models.DateField(
        verbose_name="Месяц и год оплаты"
    )
    amount = models.IntegerField(
        default=0,
        verbose_name="Сумма"
    )

    class Meta:
        verbose_name = "Оплата"
        verbose_name_plural = "Оплаты"

    def __str__(self):
        return f"Оплата {self.student} за {self.date}"


class CreateSchedule(models.Model):
    is_created = models.BooleanField(
        default=False,
        verbose_name="Расписание создано на текущую неделю"
    )
    week_number = models.IntegerField(
        default=0,
        verbose_name="Номер недели"
    )
