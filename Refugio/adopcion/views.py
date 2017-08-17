# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView

from adopcion.models import Persona, Solicitud


# Create your views here.
def index_adopcion(request):
	return HttpResponse("Pagina para Adopcion")

class SolicitudList(ListView):
	model = Solicitud 
	template_name = ''