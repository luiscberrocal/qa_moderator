from rest_framework.generics import ListAPIView

from qa_moderator.questions.api.serializers import QuestionSerializer
from qa_moderator.questions.models import Question


class QuestionListAPIView(ListAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        qs = Question.objects.filter(approved=True, viewed=False).order_by('priority')
        return qs
        

question_list_api_view = QuestionListAPIView.as_view()
