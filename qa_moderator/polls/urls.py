from django.urls import path

from qa_moderator.polls.views import PollView

app_name = "polls"
urlpatterns = [
    # ...
    path('answer/<int:pk>/', PollView.as_view(), name='poll-view'),
]
