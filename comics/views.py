from django.views.generic import TemplateView

from models import Post, PostStyle


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        if 'view' not in kwargs:
            kwargs['view'] = self
        kwargs['post_styles'] = PostStyle.objects.all()
        return kwargs


class PostView(TemplateView):
    template_name = "post.html"

    def get_context_data(self, **kwargs):
        if 'view' not in kwargs:
            kwargs['view'] = self
        kwargs['post_styles'] = PostStyle.objects.all()
        kwargs['post'] = Post.objects.get(id=kwargs["post_id"])
        return kwargs
