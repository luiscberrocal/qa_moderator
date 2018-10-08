from django.conf import settings
from django.test import TestCase

from qa_moderator.polls.adapters import JSONAdapter
from qa_moderator.polls.models import Question, Choice


class JSONAdapterTest(TestCase):

    def test_load_from_file(self):
        filename = settings.APPS_DIR.path('polls', 'tests', 'fixtures', 'poll_01.json').root
        adapter = JSONAdapter()
        adapter.load_from_file(filename)
        self.assertEqual(Question.objects.count(), 3)
        self.assertEqual(Choice.objects.count(), 12)
