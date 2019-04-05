import simple_history
from django.contrib import admin

# Register your models here.
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ExportMixin
from simple_history.admin import SimpleHistoryAdmin

from qa_moderator.questions.models import Question

class QuestionResource(resources.ModelResource):
    class Meta:
        model = Question

@admin.register(Question)
class QuestionAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    resource_class = QuestionResource
    list_display = ('id', 'event', 'moderator_num', 'approved', 'priority', 'question', 'created',)
    list_editable = ('approved', 'priority',)
    list_filter = ('approved', 'moderator_num', 'event')
    history_list_display = ["approved"]
