from django.db import models
from django.core import validators
from django.utils.html import format_html

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, null=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    def __str__(self):
        return self.author


class Contact(models.Model):
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10, unique=True)
    address = models.CharField(max_length=255)
    message = models.TextField(blank=True)
    userfile = models.FileField(upload_to="contact/", null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def show_image(self):
        if self.userfile:
            return format_html('<img src="/static/%s" width="100" />' % self.userfile)
