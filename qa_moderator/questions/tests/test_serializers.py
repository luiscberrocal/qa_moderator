from django.forms import model_to_dict
from test_plus import TestCase

from ..api.serializers import QuestionSerializer, QuestionWriteSerializer
from ..models import Question
from .factories import QuestionFactory


class TestQuestionSerializer(TestCase):

    def test_expected_fields(self):
        """
        This test verifies what fields are expected when serializing a Question
        using a QuestionSerializer.
        """
        question = QuestionFactory.create()
        serializer = QuestionSerializer(instance=question)
        question_data = serializer.data
        question_data_keys = ['id', 'approved', 'viewed', 'priority', 'question', 'created', 'moderator_num', 'event', ]
        self.assertEqual(set(question_data.keys()), set(question_data_keys))


class TestQuestionWriteSerializer(TestCase):

    def test_expected_fields(self):
        """
        This test verifies what fields are expected when serializing a Question
        using a QuestionSerializer.
        """
        question = QuestionFactory.create()
        serializer = QuestionWriteSerializer(instance=question)
        question_data = serializer.data
        question_data_keys = ['id', 'approved', 'viewed', 'priority', 'question', 'created', 'moderator_num', 'event', ]
        self.assertEqual(set(question_data.keys()), set(question_data_keys))

    def test_creation(self):
        """
        This test verifies that the serializer can create a Question in the database.
        """
        # Create a Question object to serialize
        question = QuestionFactory.create()

        # Convert the model to dictionary
        question_dict = model_to_dict(question)
        # Delete the object from the database
        question.delete()
        # Eliminate the primary key (id) from the dictionary
        question_dict.pop('id')

        serializer = QuestionWriteSerializer(data=question_dict)
        self.assertTrue(serializer.is_valid())
        serializer.save()
        self.assertEqual(Question.objects.count(), 1)

    def test_update_question(self):
        question = QuestionFactory.create(question='OLD QUESTION')

        question_dict = model_to_dict(question)

        question_dict['question'] = 'NEW QUESTION'

        serializer = QuestionWriteSerializer(data=question_dict, instance=question)
        self.assertTrue(serializer.is_valid())
        serializer.save()
        self.assertEqual(Question.objects.filter(question='NEW QUESTION').count(), 1)

    def test_serialize_many(self):
        QuestionFactory.create_batch(10)
        questions = Question.objects.all()
        serializer = QuestionWriteSerializer(questions, many=True)

        question_data_many = serializer.data

        # write_assertions(question_data_many, 'question_data_many', type_only=True)
        self.fail('Not implemented')
