from django.contrib.admin import register
from modeltranslation.admin import TabbedTranslationAdmin, TranslationStackedInline

from ..models import Assistant, Notary
from .mixin import AdminFieldMixin


class AssistantStackedInline(TranslationStackedInline):
    model = Assistant
    extra = 0


@register(Notary)
class NotaryAdmin(AdminFieldMixin, TabbedTranslationAdmin):
    list_display = ('id', 'full_name', 'get_little_photo', 'city',)
    list_display_links = ('full_name',)
    inlines = (AssistantStackedInline,)

    fieldsets = (
        ('Личная информация', {
            'fields': ('full_name', 'status', 'phone', 'photo',),

        }), ('Адрес', {
            'fields': ('region',
                       'city',
                       'address',
                       # 'notary_coordinates',
                       'latitude',
                       'longitude',
                       ),

        }),
        ('График работы', {
            'fields': ('start_day',
                       'end_day',
                       'start_time',
                       'end_time',
                       'break_start',
                       'break_end',
                       ),

        }),
        ('Выходные', {
            'fields': ('start_day_off',
                       'end_day_off',
                       ),

        }),

    )

    search_fields = ('full_name', 'region', 'city')
