from django.urls import path
from .views import NotaryListAPIView, perform_mailing

urlpatterns = [
    path('notary/', NotaryListAPIView.as_view(), name='notary'),
    path('mail/', perform_mailing, name='mail')
    ]