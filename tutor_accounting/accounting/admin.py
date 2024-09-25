from django.contrib import admin
from .models import (
    Lesson, Student, Payment,
    CreateSchedule, LessonAccounting
)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("pk", "student", "date")


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("pk", "first_name", "cost")


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("pk", "student", "date")


@admin.register(CreateSchedule)
class CreateScheduleAdmin(admin.ModelAdmin):
    list_display = ("pk", "week_number", "is_created")


@admin.register(LessonAccounting)
class LessonAccountingAdmin(admin.ModelAdmin):
    list_display = ("pk", "month", "year")
