from django.conf import settings
from django.db import models
from django.db.models import Q  # complex lookup, multiple lookup
from django.utils import timezone

# Create your models here.
User = settings.AUTH_USER_MODEL


class BlogPostQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        # lte = lesser than oe equal to
        return self.filter(publish_date__lte=now)

    def search(self, query):
        lookup = (Q(title__icontains=query)
                  | Q(content__icontains=query)
                  | Q(slug__icontains=query)
                  | Q(user__username__icontains=query)
                  | Q(user__first_name__icontains=query)
                  | Q(user__last_name__icontains=query)
                  # or whatever

                  )
        return self.filter(lookup)


class BlogPostManager(models.Manager):
    def get_queryset(self):
        return BlogPostQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().published().search(query)


class BlogPost(models.Model):
    user = models.ForeignKey(User, default=1, null=True,
                             on_delete=models.SET_NULL)
    image = models.ImageField(upload_to="image/", blank=True, null=True)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    content = models.TextField(blank=True, null=True)
    publish_date = models.DateTimeField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    objects = BlogPostManager()

    class Meta:
        ordering = ["-pk", "-publish_date", "-updated", "-timestamp"]

    def get_absolute_url(self):
        return f"/blog/{self.slug}"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"
