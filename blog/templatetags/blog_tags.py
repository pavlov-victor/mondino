from django import template

from blog.models import BlogThemes

register = template.Library()


@register.simple_tag()
def get_showing_themes():
    print(1)
    return BlogThemes.objects.filter(show_on_main=True)
