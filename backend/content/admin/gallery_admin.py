from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from content.models import Photo, PhotoSet, Video

from ..mixins import AdminFieldMixin, AdminMultiInputMixin


class PhotoAdmin(AdminFieldMixin, admin.TabularInline):
    model = Photo
    extra = 0
    template = 'admin/edit_inline/tabular_with_multi.html'

    readonly_fields = ('get_little_image',)
    fields = (('image', 'get_little_image',),)


@admin.register(PhotoSet)
class PhotoSetAdmin(AdminFieldMixin, AdminMultiInputMixin, TabbedTranslationAdmin):
    list_display = ('id', 'title', 'get_little_image', 'pub_date',)
    list_display_links = ('title',)

    search_fields = ('title',)
    readonly_fields = ('get_little_image', 'pub_date', )
    fields = ('title', 'slug', ('image', 'get_little_image',), 'pub_date',)
    inlines = (PhotoAdmin,)


@admin.register(Video)
class VideoAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'title', 'pub_date',)
    list_display_links = ('title',)

    search_fields = ('title',)
    readonly_fields = ('pub_date',)
    fields = ('title', 'link', 'pub_date',)
