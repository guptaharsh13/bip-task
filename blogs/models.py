from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=55)


class Comment(models.Model):

    author = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=55)
    body = models.TextField()
    replies = models.ManyToManyField(
        to="self", blank=True)


class Post(models.Model):

    title = models.CharField(max_length=255)
    slug = models.SlugField()
    tags = models.ManyToManyField(
        to=Tag, related_name="tags", blank=True)
    comments = models.ManyToManyField(
        to=Comment, related_name="comments", blank=True)
    author = models.ForeignKey(to=get_user_model(), on_delete=models.PROTECT)
    body = models.TextField()
    image = models.ImageField()
