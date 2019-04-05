from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView

from .serializers import QuestionSerializer, QuestionWriteSerializer
from ..models import Question


class QuestionListAPIView(ListAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        qs = Question.objects.filter(approved=True, viewed=False).order_by('priority')
        return qs


class QuestionDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    def get_object(self):
        return super(QuestionDetailAPIView, self).get_object()


class QuestionCreateAPIView(CreateAPIView):
    serializer_class = QuestionWriteSerializer
