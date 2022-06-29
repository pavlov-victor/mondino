from .models import Teammate, TeamPage
from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register


@register(Teammate)
class TeammateTR(TranslationOptions):
    fields = (
        'name',
        'position',
    )
@register(TeamPage)
class teamPageTR(TranslationOptions):
    fields = ()