from django.contrib import admin
from modeltranslation.admin import (TabbedTranslationAdmin,
                                    TranslationStackedInline)

from content.models import Document

@admin.register(Document)
class DocumentAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('title',)
    fields = ('title', 'file',)
    search_fields = ('title',)
