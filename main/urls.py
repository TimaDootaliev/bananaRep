from django.urls import path, include
# from main.views import PublicationsListView, PublicationDetailsView, CreatePublicationView, DeletePublicationView, \
#     UpdatePublicationView, PublicationViewSet
from rest_framework.routers import SimpleRouter

from main.views import *

# urlpatterns = [
#     path('publications/', PublicationsListView.as_view(), name='publications-list'),
#     path('publications/<int:pk>/', PublicationDetailsView.as_view(), name='publication-details'),
#     path('publications/create/', CreatePublicationView.as_view(), name='create-publication'),
#     path('publications/delete/<int:pk>/', DeletePublicationView.as_view(), name='delete-publication'),
#     path('publications/update/<int:pk>/', UpdatePublicationView.as_view(), name='update-publication'),
# ]

# urlpatterns = [
#     path('publications/', PublicationViewSet.as_view({'get': 'list'}), name='publications-list'),
#     path('publications/<int:pk>/', PublicationViewSet.as_view({'get': 'retrieve'}), name='publication-details'),
#     path('publications/create/', PublicationViewSet.as_view({'post': 'create'}), name='create-publication'),
#     path('publications/delete/<int:pk>/', PublicationViewSet.as_view({'delete': 'destroy'}), name='delete-publication'),
#     path('publications/update/<int:pk>/', PublicationViewSet.as_view({'put': 'update', 'patch': 'partial_update'}),
#          name='update-publication'),
# ]

router = SimpleRouter()
router.register('publications', PublicationViewSet, 'publications')
router.register('comments', CommentViewSet, 'comments')

urlpatterns = [
    path('', include(router.urls))
]


# urlpatterns = [
#     path('publications/', PublicationViewSet.as_view({'get': 'list', 'post': 'create'}), name='publications-list'),
#     path('publications/<int:pk>/', PublicationViewSet.as_view({'get': 'retrieve',
#                                                                'put': 'update',
#                                                                'patch': 'partial_update',
#                                                                'delete': 'destroy'}), name='publication-details'),
#     path('comments/', CreateCommentView.as_view(), name='comments'),
#     path('comments/update/<int:pk>', UpdateCommentView.as_view(), name='comments-update'),
#     path('comments/delete/<int:pk>', DeleteCommentView.as_view(), name='comments-delete'),
# ]



