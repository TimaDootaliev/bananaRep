from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# создаем функцию для выдачи ответа пользователю


@api_view(['GET'])
def test_view(request):
    return Response('Hello world')

