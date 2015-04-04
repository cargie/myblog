from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='blog_index'),
    url(r'^blog/(?P<slug>[-\w]+)/$', views.detail, name='blog_detail')
]