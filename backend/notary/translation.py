from modeltranslation.translator import TranslationOptions, register

from .models import Notary, City, WorkSchedule, DayOffSchedule


@register(WorkSchedule)
class WorkScheduleTranslationOptions(TranslationOptions):
    fields = ("start_day", "end_day")


@register(DayOffSchedule)
class DayOffScheduleTranslationOptions(TranslationOptions):
    fields = ("start_day_off", "end_day_off")


@register(City)
class CityTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Notary)
class NotaryTranslationOptions(TranslationOptions):
    fields = ('full_name', 'city', 'address', 'region',)
