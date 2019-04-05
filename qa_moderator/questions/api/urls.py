from django.urls import path

from qa_moderator.questions.api.views import QuestionListAPIView, QuestionCreateAPIView, QuestionDetailAPIView

app_name = "questions-api"

urlpatterns = [
    path(r'question/', QuestionListAPIView.as_view(), name='list-question'),
    path(r'^question/create/', QuestionCreateAPIView.as_view(), name='create-question'),
    path(r'^question/update/<int:pk>/', QuestionDetailAPIView.as_view(), name='update-question'),
    path(r'^question/delete/<int:pk>/', QuestionDetailAPIView.as_view(), name='delete-question'),
    path(r'^question/<int:pk>/', QuestionDetailAPIView.as_view(), name='detail-question'),
]
