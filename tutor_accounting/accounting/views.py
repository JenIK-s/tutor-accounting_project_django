from django.shortcuts import render
from .models import (
    Student, Lesson, Payment,
    CreateSchedule, LessonAccounting
)

from django.contrib.auth import get_user_model
from users.models import Schedule

import datetime
from django.contrib.admin.views.decorators import staff_member_required

User = get_user_model()


def get_week_days(year=datetime.datetime.today().year, week=datetime.datetime.now().isocalendar()[1]):
    # Находим первый день года
    first_day_of_year = datetime.datetime(year, 1, 1)

    # Находим первый день нужной недели
    first_weekday = first_day_of_year + datetime.timedelta(weeks=week - 1)

    # Получаем список дней недели
    week_days = []
    weekdays = {
        0: "Понедельник",
        1: "Вторник",
        2: "Среда",
        3: "Четверг",
        4: "Пятница",
        5: "Суббота",
        6: "Воскресенье",
    }
    for i in range(7):
        a = first_weekday + datetime.timedelta(days=i)
        b = Schedule.objects.filter(weekday=weekdays.get(i))
        elem = [f'{weekdays.get(i)} {a.strftime("%Y-%m-%d")}', sorted(b, key=lambda x: x.time)]
        week_days.append(elem)
    return week_days


@staff_member_required
def students(request):
    students_all = User.objects.filter(is_student=True)
    return render(
        request,
        "accounting/students.html",
        {
            "students": students_all
        }
    )


@staff_member_required
def students_detail(request, pk):
    student = User.objects.get(pk=pk)
    return render(
        request,
        "accounting/students_detail.html",
        {
            "student": student
        }
    )


@staff_member_required
def schedule(request):
    week = datetime.datetime.now().isocalendar()[1]
    schedule_all = get_week_days()
    if not CreateSchedule.objects.filter(week_number=week):
        for elem in schedule_all:
            for people in elem[1]:
                data = {
                    "student": people.student,
                    "date": f"{elem[0].split()[1]} {str(people.time)}"
                }
                Lesson.objects.create(**data)
        CreateSchedule.objects.create(week_number=week, is_created=True)
    else:
        print(True)

    return render(
        request,
        "accounting/schedule.html",
        {
            "week": schedule_all
        }
    )


@staff_member_required
def schedule_detail(request, pk, date, time):
    date_time = f"{date.split()[1]} {time}"
    student = User.objects.get(pk=pk)
    lesson = Lesson.objects.filter(student=student, date=date_time)
    if request.method == "POST":
        obj, created = LessonAccounting.objects.get_or_create(
            month=datetime.datetime.now().month,
            year=datetime.datetime.now().year,
        )
        if request.POST.get("action") == "conducted":
            lesson.update(conducted=True)
            obj.quantity_conducted += 1
            student.balance -= student.cost
        elif request.POST.get("action") == "paid":
            lesson.update(paid_for=True)
            obj.quantity_paid += 1
            student.balance += student.cost
        elif request.POST.get("action") == "move":
            pass
        elif request.POST.get("action") == "cancel":
            lesson.update(is_cancelled=True)
            obj.quantity_cancelled += 1
        student.save()
        obj.save()
    return render(
        request,
        "accounting/schedule_detail.html",
        {
            "lesson": lesson[0],
            "date": date,
            "time": time
        }
    )


def profile(request):
    return render(request, "accounting/profile.html")
