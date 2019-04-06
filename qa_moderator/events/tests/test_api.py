from django.forms import model_to_dict
from django.test import tag
from test_plus import TestCase

from ..api.serializers import EventSerializer
from ..models import Event
from .factories import EventFactory


class TestEventSerializer(TestCase):

    def test_expected_fields(self):
        """
        This test verifies what fields are expected when serializing a Event
        using a EventSerializer.
        """
        event = EventFactory.create()
        serializer = EventSerializer(instance=event)
        event_data = serializer.data
        event_data_keys = ['id', 'created', 'modified', 'name', 'title', 'event_date', 'office_name', 'fiscal_year',
                           'start_availability', 'end_availability', 'active', ]
        self.assertEqual(set(event_data.keys()), set(event_data_keys))

    def test_creation(self):
        """
        This test verifies that the serializer can create a Event in the database.
        """
        # Create a Event object to serialize
        event = EventFactory.create()

        # Convert the model to dictionary
        event_dict = model_to_dict(event)
        # Delete the object from the database
        event.delete()
        # Eliminate the primary key (id) from the dictionary
        event_dict.pop('id')

        serializer = EventSerializer(data=event_dict)
        self.assertTrue(serializer.is_valid())
        serializer.save()
        self.assertEqual(Event.objects.count(), 1)

    def test_update_name(self):
        event = EventFactory.create(name='OLD NAME')

        event_dict = model_to_dict(event)

        event_dict['name'] = 'NEW NAME'

        serializer = EventSerializer(data=event_dict, instance=event)
        self.assertTrue(serializer.is_valid())
        serializer.save()
        self.assertEqual(Event.objects.filter(name='NEW NAME').count(), 1)

    def test_update_title(self):
        event = EventFactory.create(title='OLD TITLE')

        event_dict = model_to_dict(event)

        event_dict['title'] = 'NEW TITLE'

        serializer = EventSerializer(data=event_dict, instance=event)
        self.assertTrue(serializer.is_valid())
        serializer.save()
        self.assertEqual(Event.objects.filter(title='NEW TITLE').count(), 1)

    def test_update_office_name(self):
        event = EventFactory.create(office_name='OLD OFFICE_NAME')

        event_dict = model_to_dict(event)

        event_dict['office_name'] = 'NEW OFFICE_NAME'

        serializer = EventSerializer(data=event_dict, instance=event)
        self.assertTrue(serializer.is_valid())
        serializer.save()
        self.assertEqual(Event.objects.filter(office_name='NEW OFFICE_NAME').count(), 1)

    @tag('TO-FIX')
    def test_serialize_many(self):
        EventFactory.create_batch(10)
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)

        event_data_many = serializer.data

        # write_assertions(event_data_many, 'event_data_many', type_only=True)
        self.fail('Not implemented')
