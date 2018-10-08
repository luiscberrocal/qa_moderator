from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
from model_utils.models import TimeStampedModel


class Poll(TimeStampedModel):
    text = models.CharField(max_length=255)
    pub_date = models.DateField()

    def __str__(self):
        return self.text


class Question(TimeStampedModel):
    poll = models.ForeignKey(Poll, verbose_name=_('poll'), related_name='questions', on_delete=models.CASCADE)
    content = models.TextField(_('content'))

    def __str__(self):
        return self.content


class Choice(TimeStampedModel):
    question = models.ForeignKey(Question, verbose_name=_('question'), related_name='choices', on_delete=models.CASCADE)
    value = models.CharField(_('value'), max_length=125)
    numeric_value = models.IntegerField(_('numeric value'), default=0)

    def __str__(self):
        return self.value


class Answer(TimeStampedModel):
    question = models.ForeignKey(Question, verbose_name=_('question'), related_name='answers',
                                 on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, verbose_name=_('choice'),
                                  related_name='answers',
                                  on_delete=models.CASCADE,
                                  null=True)
    content = models.CharField(_('content'), max_length=255, null=True)

    def __str__(self):
        if self.choice is not None:
            return self.choice.value
        elif self.content is not None:
            return self.content
        else:
            return '?????'
