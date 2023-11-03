from django.db.models.signals import pre_save
from django.dispatch import receiver
from notary.models import Notary
from geopy.geocoders import Nominatim

@receiver(pre_save, sender=Notary)
def update_coordinates(sender, instance, **kwargs):
    if instance.latitude == 'Coordinates not defined' or instance.longitude == 'Coordinates not defined':
        geolocator = Nominatim(user_agent='notary')
        location = geolocator.geocode(f'Кыргызстан, город {instance.city}, {instance.address}')
        if location:
            instance.latitude = location.latitude
            instance.longitude = location.longitude
