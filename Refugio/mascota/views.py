# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from mascota.forms import MascotaForm
from mascota.models import Mascota

# Create your views here.

def listado(request):
	lista = serializers.serialize('json', Mascota.objects.all(), fields=['nombre','sexo','edad_aproximada'])
	return HttpResponse(lista, content_type='application/json')

def index_mascota(request):
	#return HttpResponse("Index de Mascota")
	return render(request, 'mascota/index_mascota.html')

#****************************************
#*****Vistas  Basadas en Funciones*******
#****************************************	
"""def mascota_view(request):
	if request.method == 'POST':
		form = MascotaForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('mascota:mascota_listar')
	else:
		form = MascotaForm()

	return render(request, 'mascota/mascota_form.html', {'form':form})
"""

#****************************************
#*****Listas  Basadas en Funciones*******
#****************************************
"""def mascota_list(request):
	mascota = Mascota.objects.all().order_by('id')
	contexto = { 'mascotas':mascota}
	return render(request, 'mascota/mascota_list.html', contexto)

"""
#****************************************
#*****Edicion  Basadas en Funciones******
#****************************************
"""def mascota_edit(request, id_mascota):
	mascota = Mascota.objects.get(id=id_mascota)
	if request.method == 'GET':
		form = MascotaForm(instance=mascota)
	else:
		form = MascotaForm(request.POST, instance=mascota)
		if form.is_valid():
			form.save()
		return redirect('mascota:mascota_listar')
	return render(request, 'mascota/mascota_form.html',{'form':form})
"""

#****************************************
#****Eliminar  Basadas en Funciones******
#****************************************
"""def mascota_delete(request,id_mascota):
	mascota = Mascota.objects.get(id=id_mascota)
	if request.method == 'POST':
		mascota.delete()
		return redirect('mascota:mascota_listar')
	return render(request, 'mascota/mascota_delete.html',{'mascota':mascota})
"""

#****************************************
#*****Vistas  Basadas en Classes*******
#****************************************
class MascotaList(ListView):
	model = Mascota
	template_name = 'mascota/mascota_list.html'
	paginate_by = 3

#****************************************
#*****Vistas  Basadas en Classes*******
#****************************************
class MascotaCreate(CreateView):
	model = Mascota
	form_class = MascotaForm
	template_name = 'mascota/mascota_form.html'
	success_url = reverse_lazy('mascota:mascota_listar')

#****************************************
#*****Edicion  Basadas en Classes******
#****************************************
class MascotaUpdate(UpdateView):
	model = Mascota
	form_class = MascotaForm
	template_name = 'mascota/mascota_form.html'
	success_url = reverse_lazy('mascota:mascota_listar')

#****************************************
#*****Eliminar  Basadas en Classes******
#****************************************

class MascotaDelete(DeleteView):
	model = Mascota
	template_name = 'mascota/mascota_delete.html'
	success_url = reverse_lazy('mascota:mascota_listar')