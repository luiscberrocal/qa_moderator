from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

from qa_moderator.questions.models import Question


class CreateQuestionView(CreateView):
    model = Question
    template_name = 'questions/question.html'
    success_url = '/'
    fields = ('id', 'question')


create_question_view = CreateQuestionView.as_view()
