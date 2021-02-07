from django import forms
from django.utils.encoding import force_str
from django.utils.functional import cached_property
from wagtail.admin.edit_handlers import (FieldPanel, FieldRowPanel,
                                         InlinePanel, MultiFieldPanel,
                                         PageChooserPanel, StreamFieldPanel)
from wagtail.core import blocks
from wagtail.core.blocks import FieldBlock
from wagtail.core.fields import StreamField
from wagtail.core.rich_text import RichText, get_text_for_indexing
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock


class ColumnBlock(blocks.StreamBlock):
    heading = blocks.CharBlock(classname="full title")
    paragraph = blocks.RichTextBlock()
    image = ImageChooserBlock()

    class Meta:
        template = 'blog/blocks/column.html'


class TwoColumnBlock(blocks.StructBlock):

    left_column = ColumnBlock(icon='arrow-right', label='Left column content')
    right_column = ColumnBlock(
        icon='arrow-right', label='Right column content')

    class Meta:
        template = 'blog/blocks/two_column_block.html'
        icon = 'placeholder'
        label = 'Two Columns'


class CustomCharBlock(FieldBlock):

    def __init__(self, required=True, help_text=None, max_length=None, min_length=None, validators=(), **kwargs):
        # CharField's 'label' and 'initial' parameters are not exposed, as Block handles that functionality natively
        # (via 'label' and 'default')
        self.field = forms.CharField(
            required=required,
            help_text=help_text,
            max_length=max_length,
            min_length=min_length,
            validators=validators,
        )
        super().__init__(**kwargs)

    def get_searchable_content(self, value):
        return [force_str(value)]

    class Meta:
        template = 'blog/blocks/heading.html'


class CustomRichTextBlock(FieldBlock):

    def __init__(self, required=True, help_text=None, editor='default', features=None, validators=(), **kwargs):
        self.field_options = {
            'required': required,
            'help_text': help_text,
            'validators': validators,
        }
        self.editor = editor
        self.features = features
        super().__init__(**kwargs)

    def get_default(self):
        if isinstance(self.meta.default, RichText):
            return self.meta.default
        else:
            return RichText(self.meta.default)

    def to_python(self, value):
        # convert a source-HTML string from the JSONish representation
        # to a RichText object
        return RichText(value)

    def get_prep_value(self, value):
        # convert a RichText object back to a source-HTML string to go into
        # the JSONish representation
        return value.source

    @cached_property
    def field(self):
        from wagtail.admin.rich_text import get_rich_text_editor_widget
        return forms.CharField(
            widget=get_rich_text_editor_widget(self.editor, features=self.features),
            **self.field_options
        )

    def value_for_form(self, value):
        # Rich text editors take the source-HTML string as input (and takes care
        # of expanding it for the purposes of the editor)
        return value.source

    def value_from_form(self, value):
        # Rich text editors return a source-HTML string; convert to a RichText object
        return RichText(value)

    def get_searchable_content(self, value):
        # Strip HTML tags to prevent search backend from indexing them
        source = force_str(value.source)
        return [get_text_for_indexing(source)]

    class Meta:
        icon = "doc-full"
        template = 'blog/blocks/paragraph.html'