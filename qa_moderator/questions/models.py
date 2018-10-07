from django.db import models

# Create your models here.
from model_utils.models import TimeStampedModel
from simple_history.models import HistoricalRecords


class Question(TimeStampedModel):
    approved = models.BooleanField(default=False,
                                   help_text='Is approved to be displayed')
    viewed = models.BooleanField(default=False,
                                 help_text='Has already been displayed')
    priority = models.IntegerField(default=10000,
                                   help_text='Order to display questions. Lower '
                                             'number has higher priority and will be displayed first'
                                   )
    question = models.TextField()
    moderator_num = models.IntegerField(default=0,
                                        help_text='Field to separate questions '
                                                  'between moderators. Zero means not assigned')
    history = HistoricalRecords()

    def __str__(self):
        return self.question
