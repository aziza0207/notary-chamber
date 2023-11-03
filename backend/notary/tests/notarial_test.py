import pytest
from django.urls import reverse
from rest_framework import status

from notary.models import Notary


@pytest.mark.django_db
def test_mailing(api_client):
    pass
