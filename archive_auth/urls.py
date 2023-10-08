from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import RegisterView, RegisterUserView

urlpatterns = [
    path("auth/register1/", RegisterView.as_view(), name="register"),
    path("auth/register/", RegisterUserView.as_view({"post": "create"})),
    path(
        "auth/register/<int:pk>/", RegisterUserView.as_view({"patch": "partial_update"})
    ),
    path("auth/login/", TokenObtainPairView.as_view(), name="login"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="refresh-token"),
    path("auth/token/verify/", TokenVerifyView.as_view(), name="verify-token"),
]
