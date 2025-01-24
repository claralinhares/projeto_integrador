from django.urls import path

from . import views

app_name = "forms"

urlpatterns = [
    path("", views.forms, name="forms"),
    path("forms/", views.cadastro, name="cadastro"),
    path("create_event/", views.create_event, name="create_event"),
    path("scanner/<int:event_id>/", views.scanner_for_event, name="scanner_for_event"),
    path('list_events/', views.list_events, name='list_events'),
]