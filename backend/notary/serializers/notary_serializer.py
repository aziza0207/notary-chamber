
from rest_framework import serializers

from ..models import Notary


class NotarySerializer(serializers.ModelSerializer):
    start_time = serializers.SerializerMethodField()
    end_time = serializers.SerializerMethodField()
    break_start = serializers.SerializerMethodField()
    break_end = serializers.SerializerMethodField()

    class Meta:
        model = Notary
        fields = ('id',
                  'full_name',
                  'phone',
                  'photo',
                  'city',
                  'region',
                  'address',
                  "start_day",
                  "end_day",
                  "start_time",
                  "end_time",
                  "break_start",
                  "break_end",
                  "start_day_off",
                  "end_day_off",
                  'latitude', 'longitude',)

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




