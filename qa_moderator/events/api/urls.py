from django.urls import path

from .views import EventListAPIView, EventCreateAPIView, EventDetailAPIView

app_name = "events-api"

urlpatterns = [
    path(r'event/list/', EventListAPIView.as_view(), name='list-event'),
    path(r'event/create/', EventCreateAPIView.as_view(), name='create-event'),
    path(r'event/update/<int:pk>/', EventDetailAPIView.as_view(), name='update-event'),
    path(r'event/delete/<int:pk>/', EventDetailAPIView.as_view(), name='delete-event'),
    path(r'event/<int:pk>/', EventDetailAPIView.as_view(), name='event-detail'),
]
