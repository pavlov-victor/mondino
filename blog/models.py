from django.db import models

from wagtail.core.models import Page, index
from wagtail.admin.edit_handlers import FieldPanel, RichTextField, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.models import register_snippet

from .blocks import TwoColumnBlock, CustomRichTextBlock, CustomCharBlock, ImagesSliderBlock, MarkHeadingBlock


@register_snippet
class BlogThemes(models.Model):
    name = models.CharField('Название темы', max_length=100)
    description = models.CharField(
        'Краткое описание', max_length=150, default='')
    show_on_main = models.BooleanField('Показывать на главной', default=True)
    slug = models.SlugField(unique=True, max_length=80)

    panels = [
        FieldPanel('name'),
        FieldPanel('slug'),
        FieldPanel('description'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class ImagesSlider(object):
    pass


class BlogPage(Page):
    theme = models.ForeignKey(BlogThemes, models.SET_NULL, 'posts', null=True)
    post_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    description = models.CharField('Краткое описание', max_length=100)

    search_fields = Page.search_fields + [
        index.SearchField('description'),
    ]

    def get_posts(self):
        return self

    body = StreamField(
        [
            ('heading', CustomCharBlock(classname="full title")),
            ('paragraph', CustomRichTextBlock()),
            ('image', ImageChooserBlock(icon="image")),
            ('two_columns', TwoColumnBlock()),
            ('embedded_video', EmbedBlock(icon="media")),
            ('images_slider', ImagesSliderBlock()),
            ('mark_heading', MarkHeadingBlock()),
        ], null=True, blank=True
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel('post_image'),
        FieldPanel('description'),
        FieldPanel('theme'),
        StreamFieldPanel('body'),
    ]


class BlogHomePage(Page):
    pass
    # body = StreamField(
    #     [
    #         ('theme', ActualEventBlock(classname="full title")),
    #     ], null=True, blank=True
    # )
    #
    # content_panels = Page.content_panels + [
    #     StreamFieldPanel('body'),
    # ]


