from django.contrib.admin import register, ModelAdmin
from ..models import Notary
from modeltranslation.admin import TabbedTranslationAdmin
from django.utils.safestring import mark_safe


@register(Notary)
class NotaryAdmin(TabbedTranslationAdmin):
    list_display = ['id', 'full_name', 'region', 'city', 'address']
    list_display_links = ['full_name']

    search_fields = ['full_name', 'region', 'city']
    
    readonly_fields = ('get_little_photo', )
    fields = ('full_name', 'region', 'city', 'address', 'latitude', 'longitude', ('photo', 'get_little_photo'),)
    
    def get_little_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_little_photo.short_description = ""
