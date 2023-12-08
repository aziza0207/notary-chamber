from django.contrib import admin, messages
from django.contrib.admin.helpers import AdminForm
from django.http.request import HttpRequest
from django.template.response import TemplateResponse
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
    list_editable = ['is_pinned',]
    ordering = ['-is_pinned', '-date',]

    readonly_fields = ['id', 'date', 'get_little_image',]

    search_fields = ['title', 'slug']
    fields = ['title', 'slug', 'description', ('main_image', 'get_little_image',), 'video', 'is_pinned', 'date']

    actions = [make_pinned, make_unpinned]
    
    def changelist_view(self, request: HttpRequest, extra_context=None) -> TemplateResponse:
        pinned_count = News.objects.filter(is_pinned=True).count()
        if pinned_count > 2:
            message = f'Слишком много закреплённых новостей: {pinned_count}. Максимум могут быть закреплены 2 новости.'
            self.message_user(request, message=message, level=messages.WARNING)
        return super().changelist_view(request, extra_context)
