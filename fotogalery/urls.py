from django.conf.urls import patterns, include, url
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', ''),
    # url(r'^fotogalery/', include('fotogalery.foo.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
