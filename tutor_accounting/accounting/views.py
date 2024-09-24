from django.shortcuts import render
from .models import Student, Lesson, Payment


def students(request):
    students_all = Student.objects.all()
    return render(
        request,
        "accounting/students.html",
        {
            "students": students_all
        }
    )


def students_detail(request, pk):
    student = Student.objects.get(pk=pk)
    return render(
        request,
        "accounting/students_detail.html",
        {
            "student": student
        }
    )


def schedule(request):
    return render(request, "accounting/schedule.html")
