from django.contrib import admin

# Register your models here.
# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'title',
        'event_date',
        'office_name',
        'fiscal_year',
        'start_availability',
        'end_availability',
        'active',
    )
    list_filter = (
        'event_date',
        'start_availability',
        'end_availability',
        'active',
        'created',
        'modified',
    )
    search_fields = ('name',)
