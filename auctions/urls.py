from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("preview/<str:pk>", views.preview, name="preview"),
    path("edit/<str:pk>/", views.edit, name="edit"),
    path("listings", views.listings, name="listings"),
    path("delete/<str:pk>", views.delete, name="delete"),
]
