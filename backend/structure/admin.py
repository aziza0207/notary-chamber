from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin, TranslationStackedInline

from content.mixins import AdminFieldMixin
from structure.models import (Comission, ComissionWorker, GeneralAssembly, GeneralAssemblyWorker, NotaryCouncil,
                              NotaryCouncilWorker)


class GeneralAssemblyWorkerAdmin(TranslationStackedInline):
    model = GeneralAssemblyWorker
    extra = 0


@admin.register(GeneralAssembly)
class GeneralAssemblyAdmin(AdminFieldMixin, TabbedTranslationAdmin):
    list_display = ('id', 'name', 'get_little_image',)
    list_display_links = ('name',)
    inlines = (GeneralAssemblyWorkerAdmin,)
    readonly_fields = ('get_little_image',)
    fields = ('name', 'description', ('image', 'get_little_image',),)


class NotaryCouncilWorkerAdmin(TranslationStackedInline):
    model = NotaryCouncilWorker
    extra = 0


@admin.register(NotaryCouncil)
class NotaryCouncilAdmin(AdminFieldMixin, TabbedTranslationAdmin):
    list_display = ('id', 'name', 'get_little_image',)
    list_display_links = ('name',)
    inlines = (NotaryCouncilWorkerAdmin,)
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
    fields = ('name', 'description', ('image', 'get_little_image',),)
