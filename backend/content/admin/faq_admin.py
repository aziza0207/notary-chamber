from modeltranslation.admin import TabbedTranslationAdmin
from django.contrib import admin
from content.models import FAQ


@admin.register(FAQ)
class FAQAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'question',)
    list_display_links = ('question',)
    
    search_fields = ('question',)
