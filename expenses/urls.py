from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("add/", views.add_expense, name="add_expense"),
    path("edit/<int:pk>/", views.edit_expense, name="edit_expense"),
    path("delete/<int:pk>/", views.delete_expense, name="delete_expense"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("password_change/", views.password_change, name="password_change"),
    path("password_reset/", views.password_reset_request, name="password_reset"),
    path(
        "password_reset_confirm/<uidb64>/<token>/",
        views.password_reset_confirm,
        name="password_reset_confirm",
    ),
]
