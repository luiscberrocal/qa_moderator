import re

from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import UpdateView

from qa_moderator.polls.models import Poll, Question, Choice, Answer


class PollView(UpdateView):
    model = Poll
    fields = ['text']
    success_url = '/'

    def post(self, request, *args, **kwargs):
        regexp = re.compile(r'^answer_(\d+)$')
        post_data = request.POST
        for key, data in request.POST.items():
            match = regexp.match(key)
            if match:
                question_id = int(match.group(1))
                question = Question.objects.get(pk=question_id)
                choice_id = int(data)
                choice = Choice.objects.get(pk=choice_id)
                answer = Answer.objects.create(question=question, choice=choice, content=choice.value)


        return super(PollView, self).post(request, *args, **kwargs)



