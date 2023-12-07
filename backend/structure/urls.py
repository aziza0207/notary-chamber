from django.urls import path

from .views import ComissionListAPIView, GeneralAssemblyListAPIView, NotaryCouncilListAPIView

app_name = 'structure'

urlpatterns = [
    path('genral-assembly/', GeneralAssemblyListAPIView.as_view(), name='genral-assembly'),
    path('notary-council/', NotaryCouncilListAPIView.as_view(), name='notary-council'),
    path('comissions/', ComissionListAPIView.as_view(), name='comissions'),
]
