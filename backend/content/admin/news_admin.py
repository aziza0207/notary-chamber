from django.utils.safestring import mark_safe
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

    list_display = ["id", "title", "get_little_image", "is_pinned", "date", "get_little_image"]
    list_display_links = ["title"]

    readonly_fields = ["id", "date"]
    search_fields = ["title", "slug"]

    actions = [make_pinned, make_unpinned]



    def get_little_image(self, object):
        if object.main_image:
            return mark_safe(f"<img src='{object.main_image.url}' width=50>")

    get_little_image.short_description = ""


admin.site.register(News, NewsAdmin)
