from rest_framework import serializers, viewsets
from rest_framework.pagination import PageNumberPagination

from .models import Post, PostStyle



class Pagination(PageNumberPagination):
    page_size = 10
    max_page_size = 1000


class PostStyleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PostStyle
        fields = ('name', 'border_colour', 'text_colour', 'background_colour')


class PostStyleViewSet(viewsets.ModelViewSet):
    queryset = PostStyle.objects.all()
    serializer_class = PostStyleSerializer


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'blurb', 'image', 'creation_date', 'post_type', 'num_likes',
                  'style')


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-creation_date")
    serializer_class = PostSerializer
    pagination_class = Pagination


def register(router):
    router.register(r'post', PostViewSet)
    router.register(r'post_style', PostStyleViewSet)