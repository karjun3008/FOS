from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
# from . import models
# from .models import Post

# Create your views here.

def about(request):
	return render(request,'web/about.html',{})