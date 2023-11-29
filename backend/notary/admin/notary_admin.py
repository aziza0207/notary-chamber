from django.contrib.admin import register
from modeltranslation.admin import TabbedTranslationAdmin, TranslationStackedInline

from ..models import Notary, Assistant
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

    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('full_name',
    #                    'phone',
    #                    'photo',
    #                    'region',
    #                    'city',
    #                    'address',
    #                    # 'notary_coordinates',
    #                    'start_day',
    #                    'end_day',
    #                    'start_time',
    #                    'end_time',
    #                    'break_start',
    #                    'break_end',
    #                    'start_day_off',
    #                    'end_day_off',
    #                    'latitude',
    #                    'longitude',


    #                    )}
    #      ),
    # )
    search_fields = ('full_name', 'region', 'city')
