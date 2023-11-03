from modeltranslation.translator import register, TranslationOptions
from notary.models import Notary 


@register(Notary)
class NotaryTranslationOptions(TranslationOptions):
    fields = ('full_name', 'city', 'address', 'region',)
