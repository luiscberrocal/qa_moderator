from django import forms
from django.conf import settings

from qa_moderator.questions.models import Question


class QuestionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['moderator_num'].widget = forms.HiddenInput()

    class Meta:
        model = Question
        fields = ['id', 'question', 'moderator_num']

    def save(self, commit=True):
        max_num_moderators = settings.QUESTIONS_MAX_MODERATORS_NUM
        question_data = self.cleaned_data
        current_moderator = 1
        if Question.objects.count() > 0:
            last_question_moderator = Question.objects.last().moderator_num
            current_moderator = last_question_moderator + 1
            if current_moderator > max_num_moderators:
                current_moderator = 1
        question_data['moderator_num'] = current_moderator
        question = Question.objects.create(**question_data)
        return question

