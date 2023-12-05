from django.contrib import admin
from content.mixins import AdminFieldMixin
from modeltranslation.admin import TabbedTranslationAdmin, TranslationStackedInline

from structure.models import GeneralAssembly, GeneralAssemblyWorker, NotaryCouncil, NotaryCouncilWorker, Comission, ComissionWorker, NotaryCouncilDocument


class GeneralAssemblyWorkerAdmin(TranslationStackedInline):
    model = GeneralAssemblyWorker
    extra = 0


@admin.register(GeneralAssembly)
class GeneralAssemblyAdmin(AdminFieldMixin, TabbedTranslationAdmin):
    list_display = ('id', 'name', 'get_little_image',)
    list_display_links = ('name',)
    inlines = (GeneralAssemblyWorkerAdmin,)
    readonly_fields = ('get_little_image',)
    fields = ('name', 'description', ('image', 'get_little_image',), 'document',)


class NotaryCouncilWorkerAdmin(TranslationStackedInline):
    model = NotaryCouncilWorker
    extra = 0


class NotaryCouncilDocumentAdmin(TranslationStackedInline):
    model = NotaryCouncilDocument
    extra = 0


@admin.register(NotaryCouncil)
class NotaryCouncilAdmin(AdminFieldMixin, TabbedTranslationAdmin):
    list_display = ('id', 'name', 'get_little_image',)
    list_display_links = ('name',)
    inlines = (NotaryCouncilWorkerAdmin, NotaryCouncilDocumentAdmin,)
    readonly_fields = ('get_little_image',)
    fields = ('name', 'description', ('image', 'get_little_image',),)


class ComissionWorkerAdmin(TranslationStackedInline):
    model = ComissionWorker
    extra = 0


@admin.register(Comission)
class ComissionAdmin(AdminFieldMixin, TabbedTranslationAdmin):
    list_display = ('id', 'name', 'get_little_image',)
    list_display_links = ('name',)
    inlines = (ComissionWorkerAdmin,)
    readonly_fields = ('get_little_image',)
    fields = ('name', 'description', ('image', 'get_little_image',), 'document',)
