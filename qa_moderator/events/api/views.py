from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView

from .serializers import EventSerializer
from ..models import Event

class EventListAPIView(ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.all()


class EventDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def get_object(self):
        return super(EventDetailAPIView, self).get_object()


class EventCreateAPIView(CreateAPIView):
    serializer_class = EventSerializer
