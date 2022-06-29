from .models import Faq, LegalPage
from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register

@register(Faq)
class FaqTR(TranslationOptions):
    fields = ()

@register(LegalPage)
class LegalPageTR(TranslationOptions):
    fields = ()