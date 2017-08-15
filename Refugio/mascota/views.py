# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index_mascota(request):
	#return HttpResponse("Index de Mascota")
	return render(request, 'mascota/index_mascota.html')