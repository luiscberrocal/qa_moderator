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

from qa_moderator.events.models import Event

faker = FakerFactory.create()


class EventFactory(DjangoModelFactory):
    class Meta:
        model = Event

    name = LazyAttribute(lambda x: faker.text(max_nb_chars=60))
    title = LazyAttribute(lambda x: faker.text(max_nb_chars=60))
    event_date = LazyAttribute(lambda x: faker.date_time_between(start_date="-1y", end_date="now",
                                                           tzinfo=timezone(settings.TIME_ZONE)))
    office_name = LazyAttribute(lambda x: faker.text(max_nb_chars=80))
    fiscal_year = LazyAttribute(lambda o: randint(1, 100))
    start_availability = LazyAttribute(lambda x: faker.date_time_between(start_date="-1y", end_date="now",
                                                           tzinfo=timezone(settings.TIME_ZONE)))
    end_availability = LazyAttribute(lambda x: faker.date_time_between(start_date="-1y", end_date="now",
                                                           tzinfo=timezone(settings.TIME_ZONE)))
    active = Iterator([True, False])
