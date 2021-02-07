from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import RichTextField, FieldPanel


class About(Page):
    """О приложении"""

    body = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full")
    ]