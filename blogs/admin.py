from django.contrib import admin
from .models import Tag, Comment, Post


class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "added_on", "updated")
    list_display_links = ("id", "name")
    list_filter = ("added_on", "updated")
    search_fields = ("id", "name")


class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "posted_on", "updated")
    list_display_links = ("id", "title", "author")
    list_filter = ("author", "posted_on", "updated")
    search_fields = ("id", "title", "body", "author", "likes")


class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "published_on", "updated")
    list_display_links = ("id", "title", "author")
    list_filter = ("author", "published_on", "updated")
    search_fields = ("id", "title", "body", "tags",
                     "comments", "author", "likes")


# Register your models here.
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
