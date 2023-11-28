from django.contrib import admin
from ..mixins import AdminFieldMixin
from modeltranslation.admin import TabbedTranslationAdmin, TranslationStackedInline

from content.models import NotaryChamberDepartment, NotaryWorker


class NotaryWorkerAdmin(TranslationStackedInline):
    model = NotaryWorker
    extra = 0


@admin.register(NotaryChamberDepartment)
class NotaryChamberDepartmentAdmin(AdminFieldMixin, TabbedTranslationAdmin):
    list_display = ('id', 'name', 'get_little_image',)
    list_display_links = ('name',)
    inlines = (NotaryWorkerAdmin,)
    readonly_fields = ('get_little_image',)
    fields = ('name', 'description', ('image', 'get_little_image',),)
