from django.conf import settings
from django.db import models
from django.utils import tree

# Create your models here.
User = settings.AUTH_USER_MODEL


class BlogPost(models.Model):
    user = models.ForeignKey(User, default=1, null=True,
                             on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    content = models.TextField(blank=True, null=True)