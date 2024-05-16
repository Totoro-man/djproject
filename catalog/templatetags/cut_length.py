from django import template

register = template.Library()


@register.filter()
def cut_length(description, length):
    if description and len(description) > length:
        return description[:length]
    return description
