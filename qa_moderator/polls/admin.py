# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Poll, Question, Choice, Answer


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'pub_date')
    list_filter = ('pub_date', )


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'poll', 'content')
    list_filter = ('poll', )


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'value',
        'numeric_value',
    )
    list_filter = ('question', )


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'question',
        'choice',
        'content',
    )
    list_filter = ('question', 'choice')
