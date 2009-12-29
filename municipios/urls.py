# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns


urlpatterns = patterns('municipios.views',
     (r'^ajax_cidades/$','ajax_cidades'),
)
