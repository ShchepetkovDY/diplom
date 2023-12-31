import django_filters
from django.db import models
from django_filters import rest_framework

from goals.models import Goal


class GoalDateFilter(rest_framework.FilterSet):
    """ Модель Фильтр даты цели """

    class Meta:
        model = Goal
        fields = {
            "due_date": ("lte", "gte"),
            "category": ("exact", "in"),
            "status": ("exact", "in"),
            "priority": ("exact", "in"),
            #"category__board": ("exact",),
        }

    filter_overrides = {
        models.DateTimeField: {"filter_class": django_filters.IsoDateTimeFilter},
    }
