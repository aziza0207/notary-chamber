from modeltranslation.translator import TranslationOptions, register

from notary.models import Notary


@register(Notary)
class NotaryTranslationOptions(TranslationOptions):
    fields = ('full_name', 'city', 'address', 'region',)
