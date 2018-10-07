from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from qa_moderator.questions.models import Question


class CreateQuestionView(CreateView):
    model = Question
    template_name = 'questions/question.html'
    success_url = reverse_lazy('questions:thanks')
    fields = ('id', 'question')


create_question_view = CreateQuestionView.as_view()


class QuestionsDisplayView(LoginRequiredMixin, TemplateView):

    def get_template_names(self):
        if True:
            return ['questions/display.html']
        else:
            return ['questions/countdown.html']


questions_display_view = QuestionsDisplayView.as_view()
