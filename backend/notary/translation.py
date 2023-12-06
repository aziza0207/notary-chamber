from modeltranslation.translator import TranslationOptions, register

from .models import Notary, Assistant, Role


@register(Role)
class RoleTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Notary)
class NotaryTranslationOptions(TranslationOptions):
    fields = ('full_name', 'city', 'address', 'region',)


@register(Assistant)
class AssistantTranslationOptions(TranslationOptions):
    fields = ('full_name',)
