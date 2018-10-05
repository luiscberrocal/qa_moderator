from django.urls import path
from django.views.generic import TemplateView

from qa_moderator.questions.views import create_question_view

app_name = "questions"
urlpatterns = [
    path("", view=create_question_view, name="create-question"),
    path("thanks/", view=TemplateView.as_view(template_name="questions/thanx.html"), name="thanks"),
    path("schedule/", view=TemplateView.as_view(template_name="questions/schedule.html"), name="schedule"),
    path("countdown/", view=TemplateView.as_view(template_name="questions/countdown.html"), name="countdown"),
    path("qr/", view=TemplateView.as_view(template_name="questions/qr.html"), name="qr"),
]
