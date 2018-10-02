from django.urls import path
from django.views.generic import TemplateView

from qa_moderator.questions.views import create_question_view

app_name = "questions"
urlpatterns = [
    path("", view=create_question_view, name="create-question"),
    path("thanks/", view=TemplateView.as_view(template_name="questions/thanx.html"), name="thanks"),
]
