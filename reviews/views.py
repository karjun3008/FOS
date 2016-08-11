from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from .models import Comment
# from . import models
from .models import Comment

# Create your views here.

def com(request):
	abc=Comment.objects.get(pk=1)
	return render(request,'web/rev.html',{'all':abc,})