from modeltranslation.translator import translator, TranslationOptions
from .models import BlogThemes

class ThemesTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

translator.register(BlogThemes, ThemesTranslationOptions)