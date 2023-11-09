from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from ..mixins import AdminFieldMixin, AdminMultiInputMixin
from ..models import News, NewsImage


class NewsImageImageInline(AdminMultiInputMixin, admin.StackedInline):
    model = NewsImage
    extra = 0
    # readonly_fields = ('add_multiadd_button',)
    # fields = ('image', 'add_multiadd_button',)
    # list_display = ('add_multiadd_button',)


@admin.action(description="Закрепить выбранные новости")
def make_pinned(modeladmin, request, queryset):
    queryset.update(is_pinned=True)


@admin.action(description="Открепить выбранные новости")
def make_unpinned(modeladmin, request, queryset):
    queryset.update(is_pinned=False)


class NewsAdmin(AdminFieldMixin, TabbedTranslationAdmin):
    inlines = (NewsImageImageInline,)
    prepopulated_fields = {"slug": ("title",)}

    list_display = ["id", "title", "is_pinned", "date", "get_little_image"]
    list_display_links = ["title"]

    readonly_fields = ["id", "date", ]

    search_fields = ["title", "slug"]
    fields = ["title", "slug", "description", ("main_image", "get_little_image",), "video", "is_pinned", "date"]

    actions = [make_pinned, make_unpinned]


admin.site.register(News, NewsAdmin)
