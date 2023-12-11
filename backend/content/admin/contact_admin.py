from django.contrib import admin

from content.models import Contact, SocialLink


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'is_visible',)
    list_editable = ('is_visible',)
    list_display_links = ('phone',)


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'link', 'type',)
    list_display_links = ('link',)
