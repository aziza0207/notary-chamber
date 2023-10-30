from django.urls import path
from .views import NotaryListAPIView

urlpatterns = [
    path('notary/', NotaryListAPIView.as_view(), name='notary'),]