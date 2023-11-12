from django.db.models.signals import pre_save
from django.dispatch import receiver
from geopy.exc import GeopyError
from geopy.geocoders import Nominatim

from notary.models import Notary


@receiver(pre_save, sender=Notary)
def update_coordinates(sender, instance, **kwargs):
    '''The function checks the latitude and longitude fields. If either is empty, they are updated with the phrase
    'Coordinates not defined,' which indicates that they are not to be displayed on the frontend. Subsequently, it
    verifies whether the fields need to be redefined and calls the geopy service to convert the textual address into
    coordinates. However, this service often returns an 'unavailable' error, requiring a retry at a later time.
    Upon a successful response, the function overrides the field with the retrieved coordinates.'''

    coordinates = ['latitude', 'longitude']
    location = None
    for item in coordinates:
        if not instance.__getattribute__(item):
            instance.__setattr__(item, 'Coordinates not defined')
        if instance.__getattribute__(item) == 'Coordinates not defined':
            geolocator = Nominatim(user_agent='notary')
            if not location:
                try:
                    location = geolocator.geocode(f'Кыргызстан, город {instance.city}, {instance.address}')
                except GeopyError:
                    print('geopy is not available now')
            if location:
                instance.__setattr__(item, location.__getattribute__(item))
