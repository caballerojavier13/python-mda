from django.conf.urls import patterns, url


urlpatterns = patterns('pythonMDA.apps.persona.views',
            url(r'^$', 'list_personas_view', name='index_personas',),
            url(r'^json/$', 'list_personas_json', name='index_personas_json',),
            url(r'^new/$', 'new_personas_view', name='new_persona',),
            url(r'^json/new$', 'new_personas_json', name='new_personas_json',),
            url(r'^edit/$', 'edit_personas_view', name='edit_persona',),
            url(r'^delete/$', 'delete_personas_view', name='delete_persona',),
                      )
