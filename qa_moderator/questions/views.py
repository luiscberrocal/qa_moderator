from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from qa_moderator.events.models import Event
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

    def post(self, request, *args, **kwargs):
        post_data = dict()
        post_data['question'] = request.POST['question']
        try:
            event = Event.objects.get(id=self.kwargs.get('event_pk'))
            post_data['event'] = event
        except Event.DoesNotExist as e:
            raise e
        form = QuestionForm(data=post_data)
        if form.is_valid():
            form.save()
            redirect(self.success_url)
        else:
            return None
        #return super(CreateQuestionView, self).post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CreateQuestionView, self).get_context_data(**kwargs)
        try:
            event = Event.objects.get(id=self.kwargs.get('event_pk'))
            title = event.title
        except Event.DoesNotExist:
            title = 'No Event for {} event id'.format(self.kwargs.get('event_pk'))

        context['title'] = title
        return context



create_question_view = CreateQuestionView.as_view()


class QuestionsDisplayView(LoginRequiredMixin, TemplateView):

    def get_template_names(self):
        return ['questions/display.html']


questions_display_view = QuestionsDisplayView.as_view()
