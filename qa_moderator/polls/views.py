from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import UpdateView

from qa_moderator.polls.models import Poll


class PollView(UpdateView):
    model = Poll
    fields = ['text']

