from .models import Registration
from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register

@register(Registration)
class RegistrationTR(TranslationOptions):
    fields = ()
