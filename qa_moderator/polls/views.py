import re

from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView

from qa_moderator.polls.models import Poll, Question, Choice, Answer


class PollView(UpdateView):
    model = Poll
    fields = ['text']

    def get(self, request, *args, **kwargs):
        response = super(PollView, self).get(request, *args, **kwargs)
        if 'filled_poll_rci_2019' in request.COOKIES:
            return HttpResponseRedirect('/')
    
        return response


    def post(self, request, *args, **kwargs):
        regexp = re.compile(r'^answer_(\d+)$')
        for key, data in request.POST.items():
            match = regexp.match(key)
            if match:
                question_id = int(match.group(1))
                question = Question.objects.get(pk=question_id)
                choice_id = int(data)
                choice = Choice.objects.get(pk=choice_id)
                answer = Answer.objects.create(question=question, choice=choice, content=choice.value)

        response = HttpResponseRedirect('/')
        response.set_cookie('filled_poll_rci_2019', 'TRUE')
        return response



