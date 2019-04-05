from django.urls import path
from django.views.generic import TemplateView

from .views import create_question_view, questions_display_view

app_name = "questions"
urlpatterns = [
    path("", view=create_question_view, name="create-question"),
    path("<int:event_pk>/", view=create_question_view, name="create-question-event"),
    path("thanks/", view=TemplateView.as_view(template_name="questions/thanx.html"), name="thanks"),
    path("schedule/", view=TemplateView.as_view(template_name="questions/schedule.html"), name="schedule"),
    path("countdown/", view=TemplateView.as_view(template_name="questions/countdown.html"), name="countdown"),
    path("qrcloud/", view=TemplateView.as_view(template_name="questions/qrcloud.html"), name="qrcloud"),
    path("qrquestions/", view=TemplateView.as_view(template_name="questions/qrquestions.html"), name="qrquestions"),
    path("display/", view=questions_display_view, name="display"),

]
