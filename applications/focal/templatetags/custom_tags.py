from django import template
register = template.Library()


@register.filter(name='divided')
def div(a, b):
    return a/b
