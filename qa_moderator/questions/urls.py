from django.urls import path

from qa_moderator.questions.views import create_question_view

app_name = "questions"
urlpatterns = {
    path("", view=create_question_view, name="create-question"),
}
