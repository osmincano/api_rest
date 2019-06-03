from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^companies/$', views.company_list),
    url(r'^companies/(?P<id>[0-9]+)/$', views.company_detail),
    url(r'^admin/', admin.site.urls),
]

urlpatterns = format_suffix_patterns(urlpatterns)
