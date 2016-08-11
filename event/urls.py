from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.event, name='event'),
    url(r'^(?P<event_id>[0-9]+)/$', views.detevent, name='detevent'),
]
