from django.db import models


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

    class Meta:
        verbose_name = "Ученик"
        verbose_name_plural = "Ученики"

    def __str__(self):
        return self.username


class Lesson(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        verbose_name="Ученик"
    )
    date = models.DateTimeField(
        verbose_name="Дата проведения занятия"
    )
    paid_for = models.BooleanField(
        default=False,
        verbose_name="Оплата"
    )
    conducted = models.BooleanField(
        default=False,
        verbose_name="Проведено"
    )

    class Meta:
        verbose_name = "Занятие"
        verbose_name_plural = "Занятия"

    def __str__(self):
        return f"Занятие {self.student} {self.date}"



