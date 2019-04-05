from rest_framework import serializers
from qa_moderator.events.models import Event

class EventSerializer(serializers.ModelSerializer):
    """
    Standard Serializer for Event model.
    """

    class Meta:
        model = Event
        fields = ('id', 'created', 'modified', 'name', 'title', 'event_date',
                  'office_name', 'fiscal_year', 'start_availability', 'end_availability', 'active')

