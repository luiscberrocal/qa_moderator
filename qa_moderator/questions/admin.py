from django.contrib import admin

# Register your models here.
from qa_moderator.questions.models import Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'approved', 'viewed', 'priority', 'question')
    list_editable = ('approved', 'priority', 'viewed')
    list_filter = ('approved',)
