from modeltranslation.translator import TranslationOptions, register

from structure.models import (Comission, ComissionWorker, GeneralAssembly, GeneralAssemblyWorker, NotaryCouncil,
                              NotaryCouncilWorker)


@register(GeneralAssembly)
class GeneralAsemblyTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)


@register(GeneralAssemblyWorker)
class GeneralAsemblyWorkerTranslationOptions(TranslationOptions):
    fields = ('full_name', 'position',)


@register(NotaryCouncil)
class NotaryCouncilTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)


@register(NotaryCouncilWorker)
class NotaryCouncilWorkerTranslationOptions(TranslationOptions):
    fields = ('full_name', 'position',)


@register(Comission)
class ComissionTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)


@register(ComissionWorker)
class ComissionWorkerTranslationOptions(TranslationOptions):
    fields = ('full_name', 'position',)
