from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)
    slug = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name_plural = 'Categories'
        unique_together = (('name', 'slug'),)


class Comment(models.Model):
    user = models.ForeignKey(User)
    content = models.TextField()

    def __str__(self):
        return '%s' % self.user


class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    writer = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category, blank=True)
    slug = models.SlugField(unique=True, max_length=150)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return '%s' % self.title