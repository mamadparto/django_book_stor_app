from django import template

register = template.Library()

@register.filter

def lowercase(value):
    return value.lower()