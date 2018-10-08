from django.urls import path
from django.views.generic import TemplateView

from qa_moderator.polls.views import PollView

app_name = "polls"
urlpatterns = [
    # ...
    path('answer/<int:pk>/', PollView.as_view(), name='poll-view'),
    path("thanks/", view=TemplateView.as_view(template_name="polls/thanx.html"), name="poll-thanks"),
]
