from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('fb.views',
    (r'^admin/', include(admin.site.urls)),
    (r'^index/',"main"),
) 