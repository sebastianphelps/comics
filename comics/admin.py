from django.contrib import admin
from comics.models import PostStyle, Post


class PostStyleAdmin(admin.ModelAdmin):
    list_display = ('name', 'border_colour', 'text_colour', 'background_colour')


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'creation_date', 'post_type', 'num_likes')


admin.site.register(PostStyle, PostStyleAdmin)
admin.site.register(Post, PostAdmin)