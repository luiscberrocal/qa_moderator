from django.db import models

# Create your models here.
from model_utils.models import TimeStampedModel
from django.utils.translation import ugettext_lazy as _

class Event(TimeStampedModel):

    name = models.CharField(_('name'), max_length=60)
    title = models.CharField(_('title'), max_length=60)
    event_date = models.DateField(_('event date'))
    office_name = models.CharField(_('office name'), max_length=80)
    fiscal_year = models.IntegerField(_('fiscal year'))
    start_availability = models.DateTimeField(_('start availability'), null=True)
    end_availability = models.DateTimeField(_('end availability'), null=True)
    active = models.BooleanField(_('active'), default=True)

    def __str__(self):
        return self.name
