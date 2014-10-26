from django.conf.urls import patterns, url


urlpatterns = patterns('pythonMDA.apps.persona.views',
            url(r'^$', 'list_personas_view', name='index_personas',),
            url(r'^json/$', 'list_personas_json', name='index_personas_json',),
            url(r'^json/view/(?P<persona_id>[\d]+)/$', 'view_personas_json', name='view_personas_json',),
            url(r'^/new/$', 'new_personas_view', name='new_persona',),
            url(r'^json/new$', 'new_personas_json', name='new_personas_json',),
            url(r'^edit/(?P<persona_id>[\d]+)/$', 'edit_personas_view', name='edit_persona',),
            url(r'^json/edit/(?P<persona_id>[\d]+)/$', 'edit_personas_json', name='edit_personas_json',),
            url(r'^delete/(?P<persona_id>[\d]+)/$', 'delete_personas_view', name='delete_persona',),
            url(r'^json/delete/(?P<persona_id>[\d]+)/$', 'delete_personas_json', name='delete_personas_json',),
                      )
