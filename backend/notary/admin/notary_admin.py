from django.contrib.admin import register, ModelAdmin
from ..models import Notary


@register(Notary)
class NotaryAdmin(ModelAdmin):
    list_display = ["id", "full_name", "region", "city", "address"]
    list_display_links = ["full_name"]

    search_fields = ["full_name", "region", "city"]
