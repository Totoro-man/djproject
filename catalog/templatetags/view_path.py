from django import template

register = template.Library()


@register.filter()
def view_path(file_name):
    if file_name:
        return f'/media/catalog/{file_name}'
    return '#'
