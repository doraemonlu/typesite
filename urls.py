from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('photos.views',
	url(r'^index/$', 'index'),
	url(r'^photo/(\d+)/$', 'detail'),
	url(r'^photo/commit/$', 'commit'),
)
