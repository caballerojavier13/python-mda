from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.utils.functional import curry
from django.views.defaults import *
import settings


urlpatterns = patterns('',
    
    url(r'^', include('pythonMDA.apps.home.urls')),
    url(r'^persona/', include('pythonMDA.apps.persona.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
)