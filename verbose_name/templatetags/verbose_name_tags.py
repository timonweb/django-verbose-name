# verbose_name_tags.py
from django import template
from django.db.models import FieldDoesNotExist
from django.db.models.query import QuerySet

register = template.Library()

@register.filter
def label_for_field(instance, arg):
    """
    Returns a label for model field
    Supports querysets
    """
    if isinstance(instance, QuerySet):
        instance = instance.model
    try:
        return instance._meta.get_field(arg).verbose_name
    except FieldDoesNotExist:
        return ''

@register.filter
def object_verbose_name(instance):
    """
    Returns a singular verbose name for an object
    """
    return instance._meta.verbose_name

@register.filter
def object_verbose_name_plural(instance):
    """
    Returns a plural verbose name for an object
    """
    return instance._meta.verbose_name_plural