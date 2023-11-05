from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from content.models import PhotoSet, Photo, Video

from ..mixins import AdminFieldMixin


class PhotoAdmin(admin.StackedInline):
    model = Photo
    extra = 0

@admin.register(PhotoSet)
class PhotoSetAdmin(AdminFieldMixin, TabbedTranslationAdmin):
    list_display = ('id', 'title', 'get_little_image', 'pub_date',)
    list_display_links = ('title',)
    
    search_fields = ('title',)
    readonly_fields = ('get_little_image', 'pub_date', 'slug',)
    fields = ('title', 'slug', ('image', 'get_little_image',), 'pub_date',)
    inlines = (PhotoAdmin,)


@admin.register(Video)
class VideoAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'title', 'pub_date',)
    list_display_links = ('title',)
    
    search_fields = ('title',)
    readonly_fields = ('pub_date',)
    fields = ('title', 'link', 'pub_date',)

