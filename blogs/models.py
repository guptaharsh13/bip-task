from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.text import slugify
import re

# Create your models here.


def upload_path_handler(instance, filename):
    return f"{'_'.join(re.findall('[A-Z][a-z]*', instance.__class__.__name__))}s/{filename}"


class Tag(models.Model):
    name = models.CharField(max_length=55, db_index=True)
    added_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("added_on",)

    def __str__(self):
        return self.name


class Comment(models.Model):

    author = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=55)
    body = models.TextField()
    replies = models.ManyToManyField(
        to="self", blank=True)

    likes = models.ManyToManyField(
        to=get_user_model(), related_name="liked_comments", blank=True)

    posted_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-posted_on",)

    def __str__(self):
        return f"{self.title} | {self.author}"


class Post(models.Model):

    title = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(blank=True, db_index=True)
    tags = models.ManyToManyField(
        to=Tag, related_name="posts", blank=True)
    comments = models.ManyToManyField(
        to=Comment, related_name="posts", blank=True)
    author = models.ForeignKey(to=get_user_model(), on_delete=models.PROTECT)
    body = models.TextField()
    image = models.ImageField(
        upload_to=upload_path_handler, blank=True, null=True)

    likes = models.ManyToManyField(
        to=get_user_model(), related_name="liked_posts", blank=True)

    published_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-published_on",)

    def __str__(self):
        return f"{self.title} | {self.author}"


@receiver(signal=post_save, sender=Post)
def createSlug(signal, sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
        instance.save()
