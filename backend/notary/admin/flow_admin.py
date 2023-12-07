from django.contrib.admin import ModelAdmin, register
from modeltranslation.admin import TabbedTranslationAdmin

from ..models import NotaryFlow, Role


@register(NotaryFlow)
class NotaryFlowAdmin(ModelAdmin):
    list_display = ('id', 'name', '_date_range',)
    list_display_links = ('name', '_date_range',)
    

# @register(MinistryFlow)
# class MinistryFlowAdmin(ModelAdmin):
#     list_display = ('id', 'name', '_date_range',)
#     list_display_links = ('name', '_date_range',)


@register(Role)
class RoleAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('name',)
