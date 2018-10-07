
import string

from random import randint
from pytz import timezone

from django.conf import settings

from factory import Iterator
from factory import LazyAttribute
from factory import SubFactory
from factory import lazy_attribute
from factory.django import DjangoModelFactory, FileField
from factory.fuzzy import FuzzyText, FuzzyInteger
from faker import Factory as FakerFactory

from qa_moderator.questions.models import Question

faker = FakerFactory.create()


class QuestionFactory(DjangoModelFactory):
    class Meta:
        model = Question

    approved = Iterator([True, False])
    viewed = Iterator([False, True])
    priority = LazyAttribute(lambda o: randint(1, 100))
    question = LazyAttribute(lambda x: faker.paragraph(nb_sentences=3, variable_nb_sentences=True))
