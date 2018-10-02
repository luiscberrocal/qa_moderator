from rest_framework import serializers

from qa_moderator.questions.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'approved', 'priority', 'question', 'created')
