from django.contrib import admin

from notary.models import EducationalCentre, Recipient


@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name',)
    list_display_links = ('email', 'name',)
    search_fields = ('email',)


@admin.register(EducationalCentre)
class EducationalCentreAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name',)
    list_display_links = ('email', 'name',)
    search_fields = ('email',)
