import os
import uuid

from django.db import models
from django.utils.timezone import now
from colorfield.fields import ColorField


def upload_path_and_rename(instance, filename):
    name, ext = os.path.splitext(filename)
    return os.path.join("post", "%s%s" % (str(uuid.uuid4()), ext))


class PostStyle(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True, primary_key=True)
    border_colour = ColorField(blank=False, null=False)
    text_colour = ColorField(blank=False, null=False)
    background_colour = ColorField(blank=False, null=False)

    def __unicode__(self):
        return unicode(self.name)


class Post(models.Model):
    COMIC = "COMIC"
    THOUGHT = "THOUGHT"

    POST_TYPES = (
        (COMIC, "Comic"),
        (THOUGHT, "Thought"),
    )

    title = models.CharField(max_length=255, null=False, blank=False)
    blurb = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_path_and_rename, null=True, blank=True)
    creation_date = models.DateTimeField(default=now, null=False, blank=False)
    post_type = models.CharField(max_length=32, choices=POST_TYPES)
    num_likes = models.IntegerField(default=0, null=False, blank=False)
    style = models.ForeignKey(PostStyle, null=True, blank=True)

    @property
    def next(self):
        res = Post.objects.filter(
            creation_date__lt=self.creation_date
        ).order_by("-creation_date")
        if res.count() == 0:
            return None
        return res[0]

    @property
    def previous(self):
        res = Post.objects.filter(
            creation_date__gt=self.creation_date
        ).order_by("creation_date")
        if res.count() == 0:
            return None
        return res[0]

    def __unicode__(self):
        return unicode(self.title)


class PostLikes(models.Model):

    post = models.ForeignKey(Post)
    ip_address = models.IPAddressField()