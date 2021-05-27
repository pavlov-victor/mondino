from django.db import models

from wagtail.core.models import Page, index
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, RichTextField, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.models import register_snippet


@register_snippet
class Teammate(models.Model):
    """Член команды."""

    name = models.CharField('Имя', max_length=150)
    position = models.CharField('Должность', max_length=100)
    photo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('position'),
        ImageChooserPanel('photo'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Член команды'
        verbose_name_plural = 'Члены команды'


class TeamPage(Page):
    """Страница команды."""

    team_slider = StreamField(
        [
            ('image', ImageChooserBlock(icon="image")),
        ], null=True, blank=True
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('team_slider'),
    ]


# @register_snippet
# class Investors(models.Model):
#     """Инвесторы."""

#     name = models.CharField('Название', max_length=150)
#     position = models.CharField('Ценность', max_length=100)
#     photo = models.ForeignKey(
#         'wagtailimages.Image',
#         null=True,
#         blank=True,
#         on_delete=models.SET_NULL,
#         related_name='+'
#     )

#     panels = [
#         FieldPanel('name'),
#         FieldPanel('position'),
#         ImageChooserPanel('photo'),
#     ]

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name = 'Инвесторы'
#         verbose_name_plural = 'Инвесторы'
