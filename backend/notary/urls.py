from django.urls import path
from .views import NotaryListAPIView, make_and_send_message

urlpatterns = [
    path('notary/', NotaryListAPIView.as_view(), name='notary'),
    path('mail/', make_and_send_message, name='mail')
    ]