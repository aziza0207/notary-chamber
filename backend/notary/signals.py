from django.db.models.signals import pre_save
from django.dispatch import receiver
from geopy.geocoders import Nominatim

from notary.models import Notary


@receiver(pre_save, sender=Notary)
def update_coordinates(sender, instance, **kwargs):
    coordinates = ['latitude', 'longitude']
    location = None
    for item in coordinates:
        if not instance.__getattribute__(item):
            instance.__setattr__(item, 'Coordinates not defined')
        if instance.__getattribute__(item) == 'Coordinates not defined':
            geolocator = Nominatim(user_agent='notary')
            location = location if location else geolocator.geocode(f'Кыргызстан, город {instance.city}, {instance.address}')
            if location:
                instance.__setattr__(item, location.__getattribute__(item))
