from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
# from fos.forms import ContactForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
# from fos.forms import UserForm

# from . import models
from web.models import Post

# Create your views here.

def home(request):
	all_post=Post.objects.all()
	return render(request,'web/ap.html',{'all_post': all_post,})

def contact(request):
    return render(request, 'web/contact.html', {})

# def logout_user(request):
#     logout(request)
#     form = UserForm(request.POST or None)
#     context = {
#         "form": form,
#     }
#     return render(request, 'web/login.html', context)


# def login_user(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 # albums = Album.objects.filter(user=request.user)
#                 return render(request, 'web/index.html', {})
#             else:
#                 return render(request, 'web/login.html', {'error_message': 'Your account has been disabled'})
#         else:
#             return render(request, 'web/login.html', {'error_message': 'Invalid login'})
#     return render(request, 'web/login.html')


# def register(request):
#     form = UserForm(request.POST or None)
#     if form.is_valid():
#         user = form.save(commit=False)
#         username = form.cleaned_data['username']
#         password = form.cleaned_data['password']
#         user.set_password(password)
#         user.save()
#         user = authenticate(username=username, password=password)
#         # if user is not None:
#         #     if user.is_active:
#         #         login(request, user)
#         #         # albums = Album.objects.filter(user=request.user)
#         #         return render(request, 'web/ap.html', {})
#     return render(request, 'web/test.html',{"form": form,})


# def dpost(request,post_id):
# 	try:
# 		post=Post.objects.get(pk=post_id)
# 	except Pdetail.DoesNotExist:
# 		raise Http404("Post does not exist")
# 	return render(request,'web/dpost.html',{'post':post,})