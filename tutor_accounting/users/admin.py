from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Schedule


class ScheduleInline(admin.TabularInline):
    fk_name = "student"
    model = Schedule
# @admin.register(Schedule)
# class ScheduleAdmin(admin.ModelAdmin):
#     list_display = ("pk", "student", "weekday")


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ("id", "username", "first_name")
    inlines = (ScheduleInline,)
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (  # new fieldset added on to the bottom
            "Данные",  # group heading of your choice; set to None for a blank space instead of a header
            {
                "fields": (
                    "is_student",
                    "balance",
                    "cost",
                ),
            },
        ),
    )
