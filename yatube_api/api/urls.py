from django.urls import path, include
from rest_framework import routers

from .views import PostViewSet, GroupViewSet, FollowViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register('follow', FollowViewSet, basename='follow')
router.register(r'posts/(?P<id>[^/.]+)/comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
