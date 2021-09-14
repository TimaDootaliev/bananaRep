from django.shortcuts import render
# from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from rest_framework.response import Response

from main.models import Publication
# создаем функцию для выдачи ответа пользователю
from main.serializers import PublicationListSerializer, PublicationDetailSerializer


class PublicationListCreateView(ListCreateAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationListSerializer


class PublicationDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationDetailSerializer








'''
CRUD => CREATE RETRIEVE UPDATE DELETE
        CREATE READ UPDATE DESTROY
        POST GET PUT/PATCH DELETE
'''

