from django.contrib import admin
from .models import (
    Lesson, Student, Payment,
    Schedule
)


class ScheduleInline(admin.TabularInline):
    fk_name = "student"
    model = Schedule


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("pk", "student", "date")


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("pk", "first_name", "cost")
    inlines = (ScheduleInline,)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("pk", "student", "date")
