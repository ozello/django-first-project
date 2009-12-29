# -*- coding: utf-8 -*-

from municipios.models import Cidade
from django.http import HttpResponse 
from django.contrib.auth.views import login
from django.contrib.auth import REDIRECT_FIELD_NAME
#from django.contrib.auth.decorators import login_required

#@login_required
def ajax_cidades(request):

    uf = request.POST.get('estado')

    combo = ''
    
    if uf.__ne__('0'):
        dados = Cidade.objects.filter(
                    estado__abr = uf,
                    )

        for obj in dados:
            combo = combo.__add__('<option value="%(est)s">%(cid)s</option>' %{'est' : obj.id, 'cid' : obj.cidade})
            
    else:
        combo = '<option value="0">-- Primeiro selecione o estado --</option>'
    
    return HttpResponse(combo)

def logar_usuario(request, template_name='registration/login.html', redirect_field_name=REDIRECT_FIELD_NAME):
    
    #Tempo de sessão - em segundos
    #request.session.set_expiry(3600)
    
    return login(request, template_name, redirect_field_name)
    