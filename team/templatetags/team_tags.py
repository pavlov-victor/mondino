from django import template

from team.models import Teammate

register = template.Library()


@register.simple_tag()
def get_teammate():
    print(1)
    return Teammate.objects.all()
