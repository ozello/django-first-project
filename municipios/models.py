# -*- coding: utf-8 -*-
from django.db import models
    
class Pais(models.Model):
    class Meta:
        ordering = ('pais',)

    abr = models.CharField(max_length = 2)
    pais = models.CharField(max_length = 25)

    def __unicode__(self):
        return u'%s' % (self.pais)

class Estado(models.Model):
    class Meta:
        ordering = ('estado',)

    pais = models.ForeignKey(Pais)
    abr = models.CharField(max_length = 2)
    estado = models.CharField(max_length = 25)

    def __unicode__(self):
        return u'%s' % (self.estado)

class Cidade(models.Model):
    class Meta:
        ordering = ('cidade',)

    estado = models.ForeignKey(Estado)
    cidade = models.CharField(max_length = 200)
    
    def __unicode__(self):
        return u'%s' % (self.cidade)
    
