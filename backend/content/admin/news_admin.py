from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from ..mixins import AdminFieldMixin, AdminMultiInputMixin
from ..models import News, NewsImage


class NewsImageImageInline(AdminFieldMixin, admin.TabularInline):
    model = NewsImage
    extra = 0
    template = 'admin/edit_inline/tabular_with_multi.html'
    
    readonly_fields = ('get_little_image',)
    fields = (('image', 'get_little_image',),)


@admin.action(description='Закрепить выбранные новости')
def make_pinned(modeladmin, request, queryset):
    queryset.update(is_pinned=True)


@admin.action(description='Открепить выбранные новости')
def make_unpinned(modeladmin, request, queryset):
    queryset.update(is_pinned=False)


@admin.register(News)
class NewsAdmin(AdminFieldMixin, AdminMultiInputMixin, TabbedTranslationAdmin):
    inlines = (NewsImageImageInline,)
    prepopulated_fields = {'slug': ('title',)}

    list_display = ['id', 'title', 'is_pinned', 'date', 'get_little_image']
    list_display_links = ['title']

    readonly_fields = ['id', 'date', 'get_little_image',]

    search_fields = ['title', 'slug']
    fields = ['title', 'slug', 'description', ('main_image', 'get_little_image',), 'video', 'is_pinned', 'date']

    actions = [make_pinned, make_unpinned]
