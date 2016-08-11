from __future__ import unicode_literals

from django.db import models
from django import forms

class ContactForm(forms.Form):
    name= forms.CharField(required=True)
    email_address = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(required=True)

    def __str__(self):
        return self.name