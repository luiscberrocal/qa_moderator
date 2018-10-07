from django.db import models

# Create your models here.
from model_utils.models import TimeStampedModel
from simple_history.models import HistoricalRecords


class Question(TimeStampedModel):
    approved = models.BooleanField(default=False)
    viewed = models.BooleanField(default=False)
    priority = models.IntegerField(default=10000)
    question = models.TextField()
    history = HistoricalRecords()

    def __str__(self):
        return self.question
