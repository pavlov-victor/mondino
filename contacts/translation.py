from .models import Contacts
from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register

@register(Contacts)
class ContactsTR(TranslationOptions):
    fields = ()
