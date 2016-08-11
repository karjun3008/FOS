from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.
from django.db import models

# Create your models here.
class Post(models.Model):
    title= models.CharField(max_length=150)
    short_descr = models.TextField(max_length=200)
    post_image = models.TextField(max_length=200)
    post_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title

class Pdetail(models.Model):
	post=models.ForeignKey(Post, on_delete=models.CASCADE)
	post_name=models.CharField(max_length=100)
	descr=models.CharField(max_length=1000)
	
	def __str__(self):
		return self.post_name