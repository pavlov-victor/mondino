from .models import HomePage, PolicyPage
from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register


@register(HomePage)
class HomePageTR(TranslationOptions):
    fields = (
        'body',
    )
@register(PolicyPage)
class PolicyPageTR(TranslationOptions):
    fields = ()