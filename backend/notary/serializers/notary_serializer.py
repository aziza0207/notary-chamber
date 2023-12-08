from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from ..constants import StatusChoice
from ..models import Assistant, Notary


class AssistantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assistant
        fields = ('id', 'full_name',)


class NotarySerializer(serializers.ModelSerializer):
    assistants = AssistantSerializer(many=True)
    status_label = serializers.SerializerMethodField()

    start_time = serializers.SerializerMethodField()
    end_time = serializers.SerializerMethodField()
    break_start = serializers.SerializerMethodField()
    break_end = serializers.SerializerMethodField()
    start_day = serializers.SerializerMethodField()
    end_day = serializers.SerializerMethodField()
    start_day_off = serializers.SerializerMethodField()
    end_day_off = serializers.SerializerMethodField()
    class Meta:
        model = Notary
        fields = ('id',
                  'full_name',
                  'status',
                  'status_label',
                  'phone',
                #   'photo',
                  'city',
                  'region',
                  'address',
                  'start_day',
                  'end_day',
                  'start_time',
                  'end_time',
                  'break_start',
                  'break_end',
                  'start_day_off',
                  'end_day_off',
                  'latitude', 'longitude',
                  'assistants'
                  )

    def get_status_label(self, obj):
        status = obj.status
        status_label = _(StatusChoice[status.upper()].label)
        return status_label

    def get_start_day(self, obj):
        if obj.start_day:
            return _(obj.start_day)
        else:
            return obj.start_day

    def get_end_day(self, obj):
        if obj.end_day:
            return _(obj.end_day)
        else:
            return obj.end_day

    def get_start_day_off(self, obj):
        if obj.start_day_off:
            return _(obj.start_day_off)
        else:
            return obj.start_day_off

    def get_end_day_off(self, obj):
        if obj.end_day_off:
            return _(obj.end_day_off)
        else:
            return obj.end_day_off

    def get_start_time(self, obj):
        if obj.start_time:
            return obj.start_time.strftime('%H:%M')
        return ''

    def get_end_time(self, obj):
        if obj.end_time:
            return obj.end_time.strftime('%H:%M')
        return ''

    def get_break_start(self, obj):
        if obj.break_start:
            return obj.break_start.strftime('%H:%M')
        return ''

    def get_break_end(self, obj):
        if obj.break_end:
            return obj.break_end.strftime('%H:%M')
        return ''




