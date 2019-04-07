from django.urls import path
from . import views

app_name = "core-api"
urlpatterns = [
    path('app-info/', views.app_info, name='app-info'),
]
