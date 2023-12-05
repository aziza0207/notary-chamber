from modeltranslation.translator import TranslationOptions, register

from structure.models import (GeneralAssembly, GeneralAssemblyWorker, NotaryCouncil, NotaryCouncilWorker,
                              Comission, ComissionWorker, NotaryCouncilDocument)


@register(NotaryCouncilDocument)
class NotaryCouncilDocumentTranslationOptions(TranslationOptions):
    fields = ('document',)


@register(GeneralAssembly)
class GeneralAsemblyTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'document',)


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
    fields = ('name', 'description', 'document',)


@register(ComissionWorker)
class ComissionWorkerTranslationOptions(TranslationOptions):
    fields = ('full_name', 'position',)
