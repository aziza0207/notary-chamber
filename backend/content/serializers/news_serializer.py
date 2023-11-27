import random

from rest_framework import serializers

from ..models import News, NewsImage


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsImage
        fields = ('image',)


class NewsListSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ('slug', 'main_image', 'title', 'description', 'date')

    def get_description(self, obj):
        max_length = 120
        description = obj.description
        if len(description) > max_length:
            return description[:max_length] + '...'
        else:
            return description


class NewsDetailSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    recommended = serializers.SerializerMethodField()


    class Meta:
        model = News
        fields = ('main_image',
                  'title',
                  'description',
                  'video',
                  'images',
                  'date',
                  'recommended')

    def get_recommended(self, obj):
        slug = obj.slug
        queryset = News.objects.exclude(slug=slug)[:11]
        queryset_3 = random.sample(list(queryset), k=3)
        serialized_data = NewsListSerializer(queryset_3, many=True).data
        request = self.context.get('request')
        for item in serialized_data:
            image_url = item.get('main_image')
            absolute_image_url = request.build_absolute_uri(image_url)
            item['main_image'] = absolute_image_url
        return serialized_data
