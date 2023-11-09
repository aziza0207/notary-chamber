from django.db import models
from ..constants import DaysChoice

# DAYS_OF_THE_WEEK = (
#     ("1", "Пон"),
#     ("2", "Вт"),
#     ('3', 'Ср'),
#     ('4', 'Чт'),
#     ('5', 'Пт'),
#     ('6', 'Сб'),
#     ('7', 'Вс'),
#     ('8', 'Mon'),
#     ('9', 'Tue'),
#     ('10', 'Wed'),
#     ('11', 'Thu'),
#     ('12', 'Fri'),
#     ('13', 'Sat'),
#     ('14', 'Sun')
# )


class WorkSchedule(models.Model):

    start_day = models.CharField("Рабочие дни с", max_length=5,
                                 choices=DaysChoice.choices,
                                 blank=True, null=True)
    end_day = models.CharField("по", max_length=5,
                               choices=DaysChoice.choices,
                               blank=True, null=True)
    start_time = models.TimeField("Рабочее время с", blank=True, null=True)
    end_time = models.TimeField("по", blank=True, null=True)
    break_start = models.TimeField("Перерыв с", blank=True, null=True)
    break_end = models.TimeField("по", blank=True, null=True)

    class Meta:
        abstract = True


class DayOffSchedule(models.Model):
    start_day_off = models.CharField("Выходные с",
                                     max_length=5,
                                     choices=DaysChoice.choices,
                                     blank=True, null=True)
    end_day_off = models.CharField("по", max_length=5, choices=DaysChoice.choices,
                                   blank=True, null=True
                                   )

    class Meta:
        abstract = True
