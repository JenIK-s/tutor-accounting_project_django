from django.urls import path
from .views import (
    students, students_detail, schedule
)

app_name = "accounting"

urlpatterns = [
    path("", students, name="students"),
    path("students/<int:pk>/", students_detail, name="students_detail"),
    path("schedule/", schedule, name="schedule")
]
