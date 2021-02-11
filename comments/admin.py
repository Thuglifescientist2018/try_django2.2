from blog.models import User
from django.contrib import admin

from .models import UserComment
admin.site.register(UserComment)
