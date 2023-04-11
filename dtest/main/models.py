from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    rating = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Category(models.Model):
    cat_name = models.CharField(max_length=256, unique=True)


class PostType(models.TextChoices):
    POST = 'P', 'Статья'
    NEW = 'N', 'Новость'


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=PostType.choices, default=PostType.POST)
    topic = models.CharField(max_length=128)
    text = models.TextField()
    rating = models.IntegerField()
    date = models.DateTimeField()


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField()
    rating = models.IntegerField()
