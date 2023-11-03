from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from content.models import Photo, Video

from ..mixins import AdminFieldMixin


@admin.register(Photo)
class PhotoAdmin(AdminFieldMixin, TabbedTranslationAdmin):
    list_display = ('id', 'title', 'get_little_image', 'pub_date',)
    list_display_links = ('title',)
    
    search_fields = ('title',)
    readonly_fields = ('get_little_image', 'pub_date',)
    fields = ('title', ('image', 'get_little_image',), 'pub_date',)


@admin.register(Video)
class VideoAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'title', 'pub_date',)
    list_display_links = ('title',)
    
    search_fields = ('title',)
    readonly_fields = ('pub_date',)
    fields = ('title', 'link', 'pub_date',)

