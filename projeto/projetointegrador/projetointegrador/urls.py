"""
URL configuration for projetointegrador project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from forms import views
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path('forms/', include('forms.urls')),
    path("create_event/", views.create_event, name="create_event"),
    path('list_events/', views.list_events, name='list_events'),
    path('api/inscricao/validar/', views.validar_inscricao, name='validar_inscricao'),
    ]

