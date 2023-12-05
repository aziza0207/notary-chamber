from modeltranslation.translator import TranslationOptions, register

from .models import Notary, Assistant


@register(Notary)
class NotaryTranslationOptions(TranslationOptions):
    fields = ('full_name', 'city', 'address', 'region',)


@register(Assistant)
class AssistantTranslationOptions(TranslationOptions):
    fields = ('full_name',)
