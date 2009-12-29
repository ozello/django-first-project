# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
 
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    
    # urls do projeto.
    (r'^$', direct_to_template, {'template': 'index.html'}),
    (r'^municipios/', include('municipios.urls')),
    # Autenticação do usuário
    #(r'^entrar/$', 'django.contrib.auth.views.login', {'template_name': 'entrar.html'}, 'entrar'),
    (r'^entrar/$', 'municipios.views.logar_usuario', {'template_name': 'entrar.html'}, 'entrar'),
    (r'^sair/$', 'django.contrib.auth.views.logout', {'template_name': 'sair.html'}, 'sair'),
)

if settings.LOCAL:
    urlpatterns += patterns('',
        (r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
