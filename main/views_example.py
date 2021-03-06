from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
# from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView, \
    CreateAPIView, UpdateAPIView, DestroyAPIView
# from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Publication, Comment
from main.permissions import IsAuthorOrIsAdmin, IsAuthor
from main.serializers import PublicationListSerializer, PublicationDetailSerializer, CreatePublicationSerializer, \
    CommentSerializer

'''
CRUD => CREATE | RETRIEVE | UPDATE    | DELETE
        CREATE | READ     | UPDATE    | DESTROY
        POST   | GET      | PUT/PATCH | DELETE

CREATE, |LIST, RETRIEVE, |UPDATE/PARTIAL_UPDATE, | DESTROY
POST    |     GET        | PUT/PATCH             | DELETE
'''


# создаем функцию для выдачи ответа пользователю


# class PublicationListCreateView(ListCreateAPIView):
#     queryset = Publication.objects.all()
#     serializer_class = PublicationListSerializer
#
#
# class PublicationDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Publication.objects.all()
#     serializer_class = PublicationDetailSerializer


# способ написания вьюшек через функции
# @api_view(['GET'])
# def publications_list(request):
#     pubs = Publication.objects.all()  # [pub1, pub2, pub3]
#     serializer = PublicationListSerializer(pubs, many=True)  # {"id": 1, "title": "some text", "text": "another text"}
#     return Response(serializer.data)  # возвращает HTTP ответ


# class PublicationListView(APIView):
#     def get(self, request):
#         pubs = Publication.objects.all()
#         serializer = PublicationListSerializer(pubs,
#                                                many=True)
#         return Response(serializer.data)


# class PublicationsListView(ListAPIView):
#     queryset = Publication.objects.all()
#     serializer_class = PublicationListSerializer
#
#
# class PublicationDetailsView(RetrieveAPIView):
#     queryset = Publication.objects.all()
#     serializer_class = PublicationDetailSerializer
#     # lookup_url_kwarg = 'id'
#
#
# class CreatePublicationView(CreateAPIView):
#     queryset = Publication.objects.all()
#     serializer_class = CreatePublicationSerializer
#
#
# class UpdatePublicationView(UpdateAPIView):
#     queryset = Publication.objects.all()
#     serializer_class = CreatePublicationSerializer
#
#
# class DeletePublicationView(DestroyAPIView):
#     queryset = Publication.objects.all()
#     serializer_class = CreatePublicationSerializer

# TODO: Объявления создавались со статусом draft, а затем автор мог опубликовать(поменять на open)
# TODO: Черновик не отображается в общем списке - его может видеть только автор
class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = CreatePublicationSerializer
    permission_classes = [IsAuthorOrIsAdmin, ]

    # pagination_class = класс пагинации для данной вьюшки
    # paginate_by = page_size для данной вьюшки

    # def get_permissions(self):
    #     if self.action == 'create':
    #         return [IsAuthenticated()]
    #     elif self.action in ['update', 'partial_update', 'destroy']:
    #         return [IsAuthorOrIsAdmin()]
    #     return []

    def get_serializer_class(self):
        if self.action == 'list':
            return PublicationListSerializer
        elif self.action == 'retrieve':
            return PublicationDetailSerializer
        return CreatePublicationSerializer

    # def get_queryset(self):
    # request = self.request
    # queryset = super().get_queryset()
    # status = request.query_params.get('status')
    # if status is not None:
    #     queryset = queryset.filter(status=status)
    # return queryset


# http://127.0.0.1:8000/publications/?status=closed&created_at=...


# TODO: сделать комментарии, создавать комментарии может только залогиненный пользователь,
#  редактировать и удалять только автор
class CreateCommentView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {'request': self.request}


class UpdateCommentView(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthor]


class DeleteCommentView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthor]


class CommentViewSet(mixins.CreateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.UpdateModelMixin,
                     GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        return [IsAuthor()]

# TODO: пагинация, фильтрация, поиск





