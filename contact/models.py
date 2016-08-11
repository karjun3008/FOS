from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


# Create your models here.
class Contact_us(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.TextField(max_length=200)
    message = models.TextField(max_length=500)
    message_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
