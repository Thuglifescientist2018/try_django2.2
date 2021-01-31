from typing import ContextManager
from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        print(email)
        if email.endswith("edu"):
            raise forms.ValidationError(
                "This is not a valid email please dont use edu")
        return email

    def clean_content(self, *args, **kwargs):
        content = self.cleaned_data.get("content")
        print(content)
        return content

    def clean_full_name(self, *args, **kwargs):
        full_name = self.cleaned_data.get("full_name")
        print(full_name)
        return full_name
