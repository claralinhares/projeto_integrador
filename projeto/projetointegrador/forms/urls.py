from django.urls import path

from . import views

app_name = "forms"

urlpatterns = [
    path("", views.forms, name="forms"),
    path("forms/", views.cadastro, name="cadastro"),
]