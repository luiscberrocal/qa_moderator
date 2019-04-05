from django.forms import model_to_dict
from django.urls import reverse
from django_test_tools.assert_utils import write_assertions
from test_plus import TestCase

from qa_moderator.core.mixins import JWTTestMixin
from qa_moderator.questions.models import Question

from qa_moderator.questions.tests.factories import QuestionFactory
from qa_moderator.users.tests.factories import SimpleUserFactory


class TestQuestionListAPIView(JWTTestMixin, TestCase):

    def test_get(self):
        QuestionFactory.create_batch(10)
        url = reverse('questions-api:list-question')
        user = SimpleUserFactory.create()

        response = self.get_with_token(url, user)

        self.response_200(response)
        question_list_data = response.data

        write_assertions(question_list_data, 'question_list_data', type_only=True)


class TestQuestionDetailAPIView(JWTTestMixin, TestCase):

    def test_get(self):
        question = QuestionFactory.create()

        url = reverse('questions-api:detail-question', kwargs={'pk': question.pk})
        user = SimpleUserFactory.create()

        response = self.get_with_token(url, user)

        self.response_200(response)
        question_data = response.data

        #write_assertions(question_data, 'question_data', type_only=True)
        self.assertEqual(len(question_data.keys()), 8)
        self.assertIsNotNone(question_data['approved'])  # Example: True
        self.assertEqual(len(question_data['event'].keys()), 11)
        self.assertIsNotNone(question_data['event']['active'])  # Example: False
        self.assertIsNotNone(question_data['event']['end_availability'])  # Example: 2019-02-15T11:01:10-05:00
        self.assertIsNotNone(question_data['event']['event_date'])  # Example: 2018-10-12
        self.assertIsNotNone(question_data['event']['fiscal_year'])  # Example: 80
        self.assertIsNotNone(question_data['event']['id'])  # Example: 27
        self.assertIsNotNone(question_data['event']['name'])  # Example: Wide effect rate allow.
        self.assertIsNotNone(
            question_data['event']['office_name'])  # Example: Answer however receive section level too investment.
        self.assertIsNotNone(question_data['event']['start_availability'])  # Example: 2019-03-05T19:04:19-05:00
        self.assertIsNotNone(question_data['event']['title'])  # Example: Manage friend company property.
        self.assertIsNotNone(question_data['id'])  # Example: 4
        self.assertIsNotNone(question_data['moderator_num'])  # Example: 0
        self.assertIsNotNone(question_data['priority'])  # Example: 92
        self.assertIsNotNone(question_data['question'])
        self.assertIsNotNone(question_data['viewed'])  # Example: False

    def test_get_invalid_pk(self):
        url = reverse('questions-api:detail-question', kwargs={'pk': 1000000})
        user = SimpleUserFactory.create()

        response = self.get_with_token(url, user)

        self.response_404(response)
        question_invalid_data = response.data

        #write_assertions(question_invalid_data, 'question_invalid_data', type_only=False)
        self.assertEqual(question_invalid_data['detail'], 'Not found.')

    def test_put(self):
        question = QuestionFactory.create()

        url = reverse('questions-api:update-question', kwargs={'pk': question.pk})
        user = SimpleUserFactory.create()
        question_data = model_to_dict(question)
        question_data['question'] = 'VERY_NEW_VALUE'
        response = self.put_with_token(url, user, data=question_data)

        self.response_200(response)
        question_put_data = response.data

        write_assertions(question_put_data, 'question_put_data', type_only=True)

        self.assertEqual(question_put_data['question'], 'VERY_NEW_VALUE')

    def test_delete(self):
        question = QuestionFactory.create()

        url = reverse('questions-api:delete-question', kwargs={'pk': question.pk})
        user = SimpleUserFactory.create()

        response = self.delete_with_token(url, user)

        self.response_204(response)

        self.assertEqual(Question.objects.count(), 0)

class TestQuestionCreateAPIView(JWTTestMixin, TestCase):

    def test_post(self):
        question = QuestionFactory.create()

        question_dict = model_to_dict(question)
        question.delete()
        question_dict.pop('id')

        url = reverse('questions-api:create-question')

        user = SimpleUserFactory.create()

        response = self.post_with_token(url, user, data=question_dict)

        self.response_201(response)
        question_post_data = response.data

        self.assertEqual(Question.objects.count(), 1)
        #write_assertions(question_post_data, 'question_post_data', type_only=True)
        self.assertEqual(len(question_post_data.keys()), 8)
        self.assertIsNotNone(question_post_data['approved'])  # Example: True
        self.assertIsNotNone(question_post_data['event'])  # Example: 25
        self.assertIsNotNone(question_post_data['id'])  # Example: 2
        self.assertIsNotNone(question_post_data['moderator_num'])  # Example: 0
        self.assertIsNotNone(question_post_data['priority'])  # Example: 98
        self.assertIsNotNone(question_post_data[
                                 'question'])  # Example: Today part surface certain media. Pick lose establish child city vote age. Art organization employee senior. At talk guy house.
        self.assertIsNotNone(question_post_data['viewed'])  # Example: False
