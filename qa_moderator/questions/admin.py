import simple_history
from django.contrib import admin

# Register your models here.
from qa_moderator.questions.models import Question


@admin.register(Question)
class QuestionAdmin(simple_history.admin.SimpleHistoryAdmin):
    list_display = ('id', 'moderator_num', 'approved', 'priority', 'question', 'created',)
    list_editable = ('approved', 'priority',)
    list_filter = ('approved', 'moderator_num',)
    history_list_display = ["approved"]
