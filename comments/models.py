from django.db import models
from django import forms
from django.db.models.deletion import SET_NULL
from blog.models import BlogPost
from django.conf import settings
# Create your models here.


class UserComment(models.Model):
    username = models.CharField(blank=True, null=True, max_length=220)
    slug = models.SlugField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
