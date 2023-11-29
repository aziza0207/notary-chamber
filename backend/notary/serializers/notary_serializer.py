
from rest_framework import serializers

from ..models import Notary, Assistant


class AssistantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assistant
        fields = ('id', 'full_name',)


class NotarySerializer(serializers.ModelSerializer):
    start_time = serializers.SerializerMethodField()
    end_time = serializers.SerializerMethodField()
    break_start = serializers.SerializerMethodField()
    break_end = serializers.SerializerMethodField()
    assistants = AssistantSerializer(many=True)
    class Meta:
        model = Notary
        fields = ('id',
                  'full_name',
                  'status',
                  'phone',
                  'photo',
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




