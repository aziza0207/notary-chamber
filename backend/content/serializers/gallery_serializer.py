from rest_framework import serializers

from content.models import Photo, PhotoSet, Video


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'image', 'pub_date',)


class PhotoSetListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoSet
        fields = ('id', 'slug', 'title', 'image', 'pub_date',)


class PhotoSetDetailSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True)
    class Meta:
        model = PhotoSet
        fields = ('id', 'slug', 'title', 'image', 'description', 'pub_date', 'photos',)


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'title', 'link', 'pub_date',)
