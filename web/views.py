from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.http import Http404
from django.http import HttpResponse
from . import models
from .models import Post
# from .forms import UserForm


# Create your views here.

def ipost(request):
	all_post=Post.objects.all()
	return render(request,'web/ipost.html',{'all_post': all_post,})

def dpost(request,post_id):
	try:
		post=Post.objects.get(pk=post_id)
	except Pdetail.DoesNotExist:
		raise Http404("Post does not exist")
	return render(request,'web/dpost.html',{'post':post,})

# class UserFormView(request):
# 	form_class = UserForm
# 	template_name = 'web/test.html'

# 	def get(self,request):
# 		form=self.form_class(None)
# 		return render(request, self.template_name,{'form':form})

# 	def post(self,request):
# 		form=self.form_class(request.POST)

# 		if form.is_valid():

# 			user = form.save(commit=False)

# 			username=form.cleaned_data['username']
# 			password=form.cleaned_data['password']
# 			user.save()

# 			user=authenticate(username=username, password=password)

# 			if user is not None:
# 				if user.is_activate:
# 					login(request,user)
# 				return redirect('/about')

# 			return render(request, self.template_name,{'form':form})