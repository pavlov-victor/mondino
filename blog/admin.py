from django.contrib import admin
from .models import BlogThemes
from modeltranslation.admin import TranslationAdmin

class ThemesAdmin(TranslationAdmin):
    model = BlogThemes

admin.site.register(BlogThemes, ThemesAdmin)
