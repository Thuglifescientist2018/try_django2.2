from django.urls import path
from .views import comment_view
urlpattern = [
    path('', comment_view)
]
