from django.urls import path
from .views import DocumentListAPIView

urlpatterns = [
    path('documents/', DocumentListAPIView.as_view(), name='documents'), ]
