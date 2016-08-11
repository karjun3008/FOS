from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.ipost, name='ipost'),
    # url(r'^post/$', views.ipost, name='ipost'),
    url(r'^(?P<post_id>[0-9]+)/$', views.dpost, name='dpost'),
]
