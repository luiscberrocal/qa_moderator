from django.urls import path

from qa_moderator.questions.api.views import question_list_api_view


app_name = "questions-api"
urlpatterns = [
    path("", view=question_list_api_view, name="create-question-api"),
]
