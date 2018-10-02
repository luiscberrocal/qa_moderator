from rest_framework.generics import ListAPIView

from qa_moderator.questions.api.serializers import QuestionSerializer
from qa_moderator.questions.models import Question


class QuestionListAPIView(ListAPIView):
    serializer_class = QuestionSerializer


    def get_queryset(self):
        return Question.objects.all()


question_list_api_view = QuestionListAPIView.as_view()
