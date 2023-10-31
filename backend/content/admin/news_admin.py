from django.contrib.admin import register, ModelAdmin, StackedInline
from ..models import News, NewsImage


class NewsImageImageInline(StackedInline):
    model = NewsImage
    extra = 0


@register(News)
class NewsAdmin(ModelAdmin):
    inlines = (NewsImageImageInline,)
    prepopulated_fields = {"slug": ("title",)}

    list_display = ["id", "title", "date"]
    list_display_links = ["title"]

    readonly_fields = ["id", "date"]
    search_fields = ["title", "slug"]

