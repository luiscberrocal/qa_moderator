from django.contrib import admin


# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'approved', 'priority', 'question')
    list_editable = ('approved',)
    list_filter =  ('approved',)
