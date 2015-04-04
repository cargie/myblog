from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    url(r'^', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
]