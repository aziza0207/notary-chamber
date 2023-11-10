from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from django.urls import reverse
from content.models import PhotoSet, Photo, Video

from ..mixins import AdminFieldMixin, AdminFieldMixinPhotoSet


class PhotoAdmin(admin.StackedInline):
    model = Photo
    extra = 0
    template = 'admin/edit_inline/stacked_with_multi.html'



@admin.register(PhotoSet)
class PhotoSetAdmin(AdminFieldMixinPhotoSet, TabbedTranslationAdmin):

    prepopulated_fields = {"slug": ("title",)}

    list_display = ('id', 'title', 'get_little_image', 'pub_date',)
    list_display_links = ('title',)

    search_fields = ('title',)
    readonly_fields = ('get_little_image', 'pub_date', )
    fields = ('title', 'slug', ('image', 'get_little_image',), 'pub_date',)
    inlines = (PhotoAdmin,)

    def change_view(self, request, object_id, form_url="", extra_context=None):
        extra_context = extra_context or {}
        extra_context.update({
            'parent_model_name': self.__dict__.get('model').__name__,
            'parent_instance_id': object_id,
            'inline_model_name': self.inlines[0].model._meta.model_name,
            'upload_url': request.build_absolute_uri(reverse('content:upload_photo'))
        })
        
        return super().change_view(request, object_id, form_url, extra_context=extra_context)


@admin.register(Video)
class VideoAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'title', 'pub_date',)
    list_display_links = ('title',)

    search_fields = ('title',)
    readonly_fields = ('pub_date',)
    fields = ('title', 'link', 'pub_date',)
