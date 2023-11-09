from rest_framework import serializers

from ..models import Notary


class NotarySerializer(serializers.ModelSerializer):
    city = serializers.StringRelatedField()

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
