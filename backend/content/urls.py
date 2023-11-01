from django.urls import path
from .views import FAQListView

urlpatterns = [
    # path('documents/', DocumentListAPIView.as_view(), name='documents'),
    path('faq/', FAQListView.as_view(), name='faq'),
    ]
