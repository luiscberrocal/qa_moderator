from test_plus import TestCase

from qa_moderator.events.tests.factories import EventFactory
from qa_moderator.questions.forms import QuestionForm
from qa_moderator.questions.models import Question


class TestQuestionForm(TestCase):

    def test_save(self):
        event = EventFactory.create()
        question_data = dict()
        question_data['question'] = 'Why are we here?'
        question_data['event'] = event.id
        form = QuestionForm(data=question_data)
        self.assertTrue(form.is_valid())
        form.save()
        self.assertEqual(Question.object.count(), 1)
