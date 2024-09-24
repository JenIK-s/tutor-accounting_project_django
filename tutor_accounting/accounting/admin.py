from django.contrib import admin
from .models import Lesson, Student, Payment


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("pk", "student", "date")


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "cost")


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "student", "date")
