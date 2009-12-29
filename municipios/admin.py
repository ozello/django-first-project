# -*- coding: utf-8 -*-

from django.contrib import admin
from models import Estado, Cidade, Pais

admin.site.register(Pais)
admin.site.register(Estado)
admin.site.register(Cidade)
