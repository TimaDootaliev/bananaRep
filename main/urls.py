from django.urls import path

from main.views import PublicationDetailView, PublicationListCreateView

urlpatterns = [
    path('all/', PublicationListCreateView.as_view(), name='publication-list'),
    path('all/<int:pk>', PublicationDetailView.as_view(), name='publication-detail')
]
