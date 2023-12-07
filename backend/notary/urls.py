from django.urls import path

from .views import NotaryFlowListAPIView, NotaryListAPIView, NotaryStatusListView, make_and_send_message

app_name = 'notary'

urlpatterns = [
    path('notary/', NotaryListAPIView.as_view(), name='notary'),
    path('notary-status/', NotaryStatusListView.as_view(), name='notary-status'),
    path('notary-flows/', NotaryFlowListAPIView.as_view(), name='notary-flows'),
    path('mail/', make_and_send_message, name='mail')
    ]
