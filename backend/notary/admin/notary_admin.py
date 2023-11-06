from django.contrib.admin import register, ModelAdmin
from django.utils.safestring import mark_safe
from modeltranslation.admin import TabbedTranslationAdmin
from django.utils.translation import gettext_lazy as _

from ..models import Notary, City


@register(City)
class CityAdmin(TabbedTranslationAdmin):
    list_display = ["id", "name"]


@register(Notary)
class NotaryAdmin(TabbedTranslationAdmin):
    list_display = ['id', "full_name", "get_little_photo"]

    def get_little_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_little_photo.short_description = ""

    fieldsets = (
        ("Личная информация", {
            "fields": ("full_name", "phone", "photo"),

        }), ("Адрес", {
            "fields": ("region",
                       "city",
                       "address"),

        }))

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("full_name",
                       "phone",
                       "photo",
                       "region",
                       "city",
                       "address"

                       )}
         ),
    )
    search_fields = ("full_name", "region", "city")

