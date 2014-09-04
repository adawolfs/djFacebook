from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('fb.views',
    (r'^admin/', include(admin.site.urls)),
    url(r'^$', "main", name="home"),
    (r'^login/$',"login"),
    (r'^logout/$',"logout"),
    (r'^test',"test"),
) 
