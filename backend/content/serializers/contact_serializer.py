from rest_framework import serializers

from ..models import Contact, SocialLink


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'phone',)


class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = ('id', 'type', 'link',)
