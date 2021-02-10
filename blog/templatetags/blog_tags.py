from django import template

from blog.models import BlogThemes, BlogPage

register = template.Library()


@register.simple_tag()
def get_showing_themes():
    print(1)
    return BlogThemes.objects.filter(show_on_main=True)


@register.simple_tag()
def get_all_posts():
    print(1)
    return BlogPage.objects.all()


