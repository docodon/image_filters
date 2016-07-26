from django.conf.urls import patterns, url
from create_images import views

urlpatterns = patterns('',
        url(r'^home/$',views.index.as_view(),name='home'),
        )
