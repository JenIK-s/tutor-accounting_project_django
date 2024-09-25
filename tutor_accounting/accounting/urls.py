from django.urls import path
from .views import (
    students, students_detail, schedule,
    schedule_detail,
)

app_name = "accounting"

urlpatterns = [
    path("students/", students, name="students"),
    path("students/<int:pk>/", students_detail, name="students_detail"),
    path("schedule/", schedule, name="schedule"),
    path("schedule/<int:pk>_<str:date>_<str:time>", schedule_detail, name="schedule_detail")
]
