from django.conf.urls import patterns, url


urlpatterns = patterns('pythonMDA.apps.home.views',
            url(r'^$', 'index_view', name='vista_principal',),
                      )
