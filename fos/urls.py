"""fos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    # url(r'^register/$', include('web.urls')),
    # url(r'^login_user/$', views.login_user, name='login_user'),
    # url(r'^logout_user/$', views.logout_user, name='logout_user'),
    # url(r'^reviews/', include('reviews.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^post/', include('web.urls')),
    url(r'^about/$', include('about.urls')),
    url(r'^events/', include('event.urls')),
    url(r'^$','fos.views.home', name='home'),
    # url(r'^register/','fos.views.register', name='register'),
    url(r'^home/$','fos.views.home', name='home'),
    url(r'^contact/$', 'fos.views.contact',name='contact'),

]