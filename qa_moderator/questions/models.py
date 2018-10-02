from django.db import models

# Create your models here.
from model_utils.models import TimeStampedModel


class Question(TimeStampedModel):
    approved = models.BooleanField(default=False)
    viewed = models.BooleanField(default=False)
    priority = models.IntegerField(default=100)
    question = models.TextField()


    def __str__(self):
        return self.question


