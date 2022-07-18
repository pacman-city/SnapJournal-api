from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.viewsets import GenericViewSet
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django.shortcuts import get_object_or_404
from rest_framework import mixins

from posts.models import Post, Group, Follow, Comment
from .permissions import IsOwnerOrReadOnly
from .serializers import (
    PostSerializer,
    GroupSerializer,
    FollowSerializer,
    CommentSerializer)


class PostViewSet(ModelViewSet):
    """POST"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(ModelViewSet):
    """COMMENT"""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get("id"))
        return post.comments

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('id'))
        serializer.save(post=post)

    def perform_destroy(self, serializer):
        if serializer.author != self.request.user:
            raise PermissionDenied('Not allowed')
        super(CommentViewSet, self).perform_update(serializer)


class GroupViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   GenericViewSet):
    """GROUP"""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    GenericViewSet):
    """FOLLOW"""
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)
