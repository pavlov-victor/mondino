from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import RichTextField, FieldPanel


class HomePage(Page):
    """Главная страница."""

    body = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full")
    ]
