from django.urls import path
from main.views import *


urlpatterns = [
    path('publications/', ListAPIView.as_view(), name='publications-list'),
    path('publications/<int:pk>', RetrieveAPIView.as_view(), name='publication-details'),
    path('publications/create/', CreatePublicationView.as_view(), name='create-publication'),
    path('publications/delete/', DeletePublicationView.as_view(), name='delete-publication'),
    path('publications/update/<int:pk>/', UpdatePublicationView.as_view(), name='update-publication')
]

