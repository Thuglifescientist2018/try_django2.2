from django import forms
from .models import BlogPost


class BlogPostForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)


class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost  # its necessary to link the model BlogPost to have connection with it
        fields = ['title', 'slug', 'content']

    def clean_title(self, *args, **kwargs):
        instance = self.instance
        title = self.cleaned_data.get("title")
        qs = BlogPost.objects.filter(title__iexact=title)
        if instance is not None:  # we ignore the old instance update the data due to which
            # we are not gonna be getting title already exists error i think slug updates fine after adding instance=obj in the update view
            qs = qs.exclude(pk=instance.pk)  # id = instance of id
        if qs.exists():
            raise forms.ValidationError(
                "This title has been already taken")
        return title
