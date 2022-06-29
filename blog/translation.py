from .models import BlogThemes, BlogPage, ImagesSlider, BlogHomePage
from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register

@register(BlogThemes)
class BlogThemesTR(TranslationOptions):
    fields = ('name', 'description')

@register(BlogPage)
class BlogPageTR(TranslationOptions):
    fields = ('description', 'body')

# @register(ImagesSlider)
# class ImagesSliderTR(TranslationOptions):
#     fields = ()

@register(BlogHomePage)
class BlogHomePageTR(TranslationOptions):
    fields = ()
