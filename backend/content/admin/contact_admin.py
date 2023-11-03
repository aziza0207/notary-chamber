from django.contrib import admin
from content.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'is_visible',)
    list_editable = ('is_visible',)
    list_display_links = ('phone',)
