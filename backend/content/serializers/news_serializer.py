from rest_framework import serializers
from ..models import News


class NewsListSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ("slug", "main_image", "title", "description")

    def get_description(self, obj):
        max_length = 120
        description = obj.description
        if len(description) > max_length:
            return description[:max_length] + "..."
        else:
            return description


class NewsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        exclude = ("id", )
