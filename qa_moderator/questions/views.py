from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from qa_moderator.questions.forms import QuestionForm
from qa_moderator.questions.models import Question


class CreateQuestionView(CreateView):
    model = Question
    success_url = reverse_lazy('questions:thanks')
    #fields = ('id', 'question')
    form_class = QuestionForm

    def get_template_names(self):
        return ['questions/question.html']
        #if settings.QUESTIONS_ACTIVE:
           # return ['questions/question.html']
        # else:
          #  return ['questions/countdown.html']


create_question_view = CreateQuestionView.as_view()


class QuestionsDisplayView(LoginRequiredMixin, TemplateView):

    def get_template_names(self):
        return ['questions/display.html']


questions_display_view = QuestionsDisplayView.as_view()
