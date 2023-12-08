from django.contrib.admin import register
from modeltranslation.admin import TabbedTranslationAdmin, TranslationStackedInline

from import_export import resources, fields
from import_export.admin import ImportMixin

from ..models import Assistant, Notary
from .mixin import AdminFieldMixin


class NotaryResource(resources.ModelResource):
    id = fields.Field(column_name='id', attribute='id')
    full_name = fields.Field(column_name='ФИО нотариуса', attribute='full_name')
    region = fields.Field(column_name='Регион', attribute='region')
    city = fields.Field(column_name='Город', attribute='city')
    address = fields.Field(column_name='Адрес', attribute='address')
    phone = fields.Field(column_name='Телефон', attribute='phone')
    email = fields.Field(column_name='Email', attribute='email')

    class Meta:
        model = Notary
        fields = ('id', 'full_name', 'region', 'city', 'address', 'phone', 'email',)


class AssistantStackedInline(TranslationStackedInline):
    model = Assistant
    extra = 0


@register(Notary)
class NotaryAdmin(AdminFieldMixin, ImportMixin, TabbedTranslationAdmin):
    list_display = ('id', 'full_name', 'city', 'status',)
    list_display_links = ('full_name',)
    inlines = (AssistantStackedInline,)
    resource_class = NotaryResource

    fieldsets = (
        ('Личная информация', {
            'fields': ('full_name', 'status', 'phone', 'email',),

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
