from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django import http
from django.http import Http404
from django.shortcuts import render, get_object_or_404, resolve_url
from .models import BlogPost
from .forms import BlogPostModelForm
# Create your views here.


# CRUD
# GET -> Retrieve / List
# POST -> Creatre / Update / Delete
# Create Retrieve  Update Delete

def blog_post_list_view(request):
    # List out objects
    # Could be search
    qs = BlogPost.objects.all()  # queryset => list of python objects
    template_name = "list.html"
    context = {'object_list': qs}
    return render(request, template_name, context)


# @login_required (shows error)
@staff_member_required  # Shows django admin login page for staff
def blog_post_create_view(request):
    # Create Object
    # ? use a form
    form = BlogPostModelForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        obj = form.save(commit=False)
        # Here I can manipulate obj with .title or whatever in the model
        obj.save()
        form = BlogPostModelForm()
    template_name = "form.html"
    context = {'form': form}
    return render(request, template_name, context)


def blog_post_detail_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "detail.html"
    context = {'object': obj, 'form': None}
    return render(request, template_name, context)


def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "update.html"
    context = {'object': obj, 'form': None}
    return render(request, template_name, context)


def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "delete.html"
    context = {'object': obj, 'form': None}
    return render(request, template_name, context)
