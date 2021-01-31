from django.shortcuts import render
from .forms import ContactForm


def home(request):
    template_name = "home.html"
    return render(request, template_name)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():

        form = ContactForm()
    template_name = "form.html"
    context = {"title": "Contact Us",
               "form": form
               }
    return render(request, template_name, context)
