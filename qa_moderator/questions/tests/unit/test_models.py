from django.forms import model_to_dict
from django.test import TestCase

from qa_moderator.events.tests.factories import EventFactory
from qa_moderator.questions.models import Question
from qa_moderator.questions.tests.factories import QuestionFactory


class TestCaseQuestion(TestCase):

    def test_create(self):
        """
        Test the creation of a Question model using a factory
        """
        question = QuestionFactory.create()
        self.assertEqual(Question.objects.count(), 1)

    def test_create_fixed_event(self):
        """
        Test the creation of a Question model using a factory
        """
        event = EventFactory.create()
        question = QuestionFactory.create(event=event)
        self.assertEqual(Question.objects.count(), 1)

    def test_create_batch(self):
        """
        Test the creation of 5 Question models using a factory
        """
        questions = QuestionFactory.create_batch(5)
        self.assertEqual(Question.objects.count(), 5)
        self.assertEqual(len(questions), 5)

    def test_attribute_count(self):
        """
        Test that all attributes of Question server are counted. It will count the primary key and all editable attributes.
        This test should break if a new attribute is added.
        """
        question = QuestionFactory.create()
        question_dict = model_to_dict(question)
        self.assertEqual(len(question_dict.keys()), 7)

    def test_attribute_content(self):
        """
        Test that all attributes of Question server have content. This test will break if an attributes name is changed.
        """
        question = QuestionFactory.create()
        self.assertIsNotNone(question.id)
        self.assertIsNotNone(question.created)
        self.assertIsNotNone(question.modified)
        self.assertIsNotNone(question.approved)
        self.assertIsNotNone(question.viewed)
        self.assertIsNotNone(question.priority)
        self.assertIsNotNone(question.question)
        self.assertIsNotNone(question.moderator_num)
        self.assertIsNotNone(question.event)
