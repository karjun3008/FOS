from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=250)
    place = models.CharField(max_length=250)
    short_descr = models.TextField(max_length=500)
    event_image = models.TextField(max_length=200)
    event_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Devent(models.Model):
	event=models.ForeignKey(Event, on_delete=models.CASCADE)
	event_image = models.TextField(max_length=500)
	event_name=models.CharField(max_length=100)
	descr=models.CharField(max_length=1000)

	
	def __str__(self):
		return self.event_name