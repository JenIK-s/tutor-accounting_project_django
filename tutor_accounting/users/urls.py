from django.contrib.auth.views import (
    # LoginView,
    LogoutView,
)
from django.urls import path
from .views import SignIn

app_name = 'users'

urlpatterns = [
    path(
        'logout/',
        LogoutView.as_view(),
        name='logout'
    ),
    path(
        'signin/',
        SignIn,
        name='signin'
    )
]
