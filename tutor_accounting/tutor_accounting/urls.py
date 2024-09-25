from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("accounting.urls", namespace="accounting")),
    path("users/", include("users.urls", namespace="users")),
]
