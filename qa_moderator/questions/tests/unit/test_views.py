from django.test import TestCase, Client, tag
from django.urls import reverse

from qa_moderator.events.tests.factories import EventFactory


class TestCreateQuestionView(TestCase):

    @tag('TO-FIX')
    def test_post(self):
        event = EventFactory.create()
        url = reverse('questions:create-question-event', kwargs={'event_pk': event.id})
        client = Client()
        post_data = dict()
        post_data['question'] = 'Hello?'
        response = client.post(url, data=post_data)
        self.assertEqual(response.status_code, 200)
