from django.urls import path
from .views import (
    index
)

app_name = 'accounting'

urlpatterns = [
    path('', index, name='index'),
]
