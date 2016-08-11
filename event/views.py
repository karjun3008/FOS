from django.shortcuts import render
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from . import models
from .models import Event
from .models import Devent


# Create your views here.
def event(request):
	all_event=Event.objects.all()
	return render(request,'web/events.html',{'all_event': all_event,})

def detevent(request,event_id):
	event = get_object_or_404(Event , pk=event_id)
	return render(request,'web/dpost.html',{'event':event,})