from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import RichTextField, FieldPanel


class HomePage(Page):
    """Главная страница."""

    body = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full")
    ]

    def get_context(self, request, *args, **kwargs):
        context = super(HomePage, self).get_context(request, *args, **kwargs)
        # context['posts'] = self.posts
        context['blog_page'] = self

        context['menuitems'] = self.get_children().filter(
            live=True, show_in_menus=True)

        return context