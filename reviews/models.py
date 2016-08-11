from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Comment(models.Model):
    # post = models.ForeignKey('blog.Post', related_name='comments')
    name = models.CharField(max_length=200)
    email_id = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text