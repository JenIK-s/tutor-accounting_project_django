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
        return self.first_name


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
        verbose_name="Оплачено"
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


class Payment(models.Model):
    student = models.ForeignKey(
        Student,
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


class Schedule(models.Model):
    choises = (
        ("Не выбрано", "Не выбрано"),
        ("Понедельник", "Создан"),
        ("Вторник", "Собирается"),
        ("Среда", "В пути"),
        ("Четверг", "Доставлено"),
        ("Пятница", "Получено"),
        ("Суббота", "Суббота"),
        ("Воскресенье", "Воскресенье")
    )
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        verbose_name="Ученик"
    )
    weekday = models.CharField(
        max_length=50,
        default="Не выбрано",
        choices=choises,
        verbose_name="День недели",
    )
    time = models.TimeField(
        verbose_name="Время"
    )

    class Meta:
        verbose_name = "День занятия"
        verbose_name_plural = "Дни занятий"

    def __str__(self):
        return f"{self.student} {self.weekday}"
