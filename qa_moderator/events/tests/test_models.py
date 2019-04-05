from django.test import TestCase
from django.forms.models import model_to_dict
from django.db import IntegrityError
from django.conf import settings

from qa_moderator.events.models import Event
from qa_moderator.events.tests.factories import EventFactory


class TestCaseEvent(TestCase):

    def test_create(self):
        """
        Test the creation of a Event model using a factory
        """
        event = EventFactory.create()
        self.assertEqual(Event.objects.count(), 1)

    def test_create_batch(self):
        """
        Test the creation of 5 Event models using a factory
        """
        events = EventFactory.create_batch(5)
        self.assertEqual(Event.objects.count(), 5)
        self.assertEqual(len(events), 5)


    def test_attribute_count(self):
        """
        Test that all attributes of Event server are counted. It will count the primary key and all editable attributes.
        This test should break if a new attribute is added.
        """
        event = EventFactory.create()
        event_dict = model_to_dict(event)
        self.assertEqual(len(event_dict.keys()), 9)



    def test_attribute_content(self):
        """
        Test that all attributes of Event server have content. This test will break if an attributes name is changed.
        """
        event = EventFactory.create()
        self.assertIsNotNone(event.id)
        self.assertIsNotNone(event.created)
        self.assertIsNotNone(event.modified)
        self.assertIsNotNone(event.name)
        self.assertIsNotNone(event.title)
        self.assertIsNotNone(event.event_date)
        self.assertIsNotNone(event.office_name)
        self.assertIsNotNone(event.fiscal_year)
        self.assertIsNotNone(event.start_availability)
        self.assertIsNotNone(event.end_availability)
        self.assertIsNotNone(event.active)
