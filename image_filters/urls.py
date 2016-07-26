from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings # New Import
from django.conf.urls.static import static # New Import


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'image_filters.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^',include('create_images.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',(r'^media/(?P<path>.*)','serve',{'document_root': settings.MEDIA_ROOT}), )

if not settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
