from django.contrib import admin
from modeltranslation.admin import (TabbedTranslationAdmin,
                                    TranslationStackedInline)

from content.models import Category, Document


class InlineDocumentAdmin(TranslationStackedInline):
    model = Document
    extra = 0


@admin.register(Category)
class CategoryAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('title',)
    search_fields = ('title',)
    inlines = (InlineDocumentAdmin,)


@admin.register(Document)
class DocumentAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'title', 'category',)
    list_display_links = ('title',)
    fields = ('title', 'category', 'file',)
    search_fields = ('title',)
