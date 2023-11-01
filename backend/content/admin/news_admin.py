# import django.contrib.admin import register, ModelAdmin, StackedInline
from django.contrib import admin
from ..models import News, NewsImage


class NewsImageImageInline(admin.StackedInline):
    model = NewsImage
    extra = 0


@admin.action(description="Закрепить выбранные новости")
def make_pinned(modeladmin, request, queryset):
    queryset.update(is_pinned=True)


@admin.action(description="Открепить выбранные новости")
def make_unpinned(modeladmin, request, queryset):
    queryset.update(is_pinned=False)


class NewsAdmin(admin.ModelAdmin):
    inlines = (NewsImageImageInline,)
    prepopulated_fields = {"slug": ("title",)}

    list_display = ["id", "title", "is_pinned", "date"]
    list_display_links = ["title"]

    readonly_fields = ["id", "date"]
    search_fields = ["title", "slug"]

    actions = [make_pinned, make_unpinned]


admin.site.register(News, NewsAdmin)
