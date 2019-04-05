from rest_framework import serializers

from qa_moderator.questions.models import Question


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('id', 'approved', 'viewed',
                  'priority', 'question', 'created', 'moderator_num',
                  'event')

class QuestionWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('id', 'approved', 'viewed',
                  'priority', 'question', 'created', 'moderator_num',
                  'event')
