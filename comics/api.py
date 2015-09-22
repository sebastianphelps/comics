import logging

from rest_framework import serializers, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import detail_route
from rest_framework.exceptions import ValidationError, PermissionDenied
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.filters import BaseFilterBackend, OrderingFilter

from ipware.ip import get_ip, get_real_ip

from .models import Post, PostStyle, PostLikes

log = logging.getLogger("comics")


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


class TagFilter(BaseFilterBackend):
    # The URL query parameter used for the search.
    search_param = "search"

    def get_search_terms(self, request):
        params = request.query_params.get(self.search_param, '')
        return params.replace(',', ' ').split()

    def filter_queryset(self, request, queryset, view):
        search_terms = self.get_search_terms(request)
        if len(search_terms) == 0:
            return queryset
        return queryset.filter(tags__name__in=search_terms).distinct()


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = Pagination
    filter_backends = (TagFilter, OrderingFilter)
    ordering_fields = ('creation_date', 'num_likes')

    @detail_route(methods=['get'], permission_classes=[AllowAny])
    def like(self, request, pk=None):
        #ip_address = get_ip(request)
        ip_address = get_real_ip(request)
        log.debug(ip_address)
        if ip_address is None:
            log.debug("No IP address found")
            raise ValidationError("No IP address found")
        post_likes = PostLikes.objects.filter(ip_address=ip_address, post__id=pk).count()
        log.debug("post_id=%s post_likes=%s", pk, post_likes)
        if post_likes == 0:
            log.debug("Liking post %s" % pk)
            post = Post.objects.get(pk=pk)
            PostLikes.objects.create(post=post, ip_address=ip_address)
            post.num_likes += 1
            post.save()
            return Response({"num_likes": post.num_likes})
        else:
            log.debug("Already liked")
            raise PermissionDenied("Already liked")


def register(router):
    router.register(r'post', PostViewSet)
    router.register(r'post_style', PostStyleViewSet)