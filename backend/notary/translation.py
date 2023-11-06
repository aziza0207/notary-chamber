from modeltranslation.translator import TranslationOptions, register

from .models import Notary, City


@register(Notary)
class NotaryTranslationOptions(TranslationOptions):
    fields = ('full_name', 'city', 'address', 'region',)


@register(City)
class CityTranslationOptions(TranslationOptions):
    fields = ('name', )
