from django import template

register = template.Library()


@register.filter
def getkey(obj, key, default=""):
    return getattr(obj, key, default)
