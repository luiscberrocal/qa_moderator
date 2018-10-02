from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

from qa_moderator.questions.models import Question


class CreateQuestionView(CreateView):
    model = Question
