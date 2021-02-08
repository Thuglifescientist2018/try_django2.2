from django.shortcuts import render
from .forms import ContactForm
from blog.models import BlogPost


def home(request):
    my_title = "Welcome to try Django..."
    qs = BlogPost.objects.all().published()
    if request.user.is_authenticated:
        my_qs = BlogPost.objects.filter(user=request.user)
        qs = (qs | my_qs).distinct()
    context = {"title": my_title, 'blog_list': qs}
    return render(request, "home.html", context)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():

        form = ContactForm()
    template_name = "form.html"
    context = {"title": "Contact Us",
               "form": form
               }
    return render(request, template_name, context)
