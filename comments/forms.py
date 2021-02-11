from django import forms
from .models import UserComment


class UserCommentModelForm(forms.ModelForm):
    class Meta:
        model = UserComment
        fields = ["username", "slug", "comment"]
