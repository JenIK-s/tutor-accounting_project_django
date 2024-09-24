from django.db import models
from users.models import CustomUser


class Lesson(models.Model):
    student = models.ForeignKey(
        CustomUser,
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

