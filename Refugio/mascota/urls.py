from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from mascota.views import index_mascota,listado, MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete

urlpatterns = [
    url(r'^$', login_required(index_mascota), name='index_mascota'),
    url(r'^nuevo$', login_required(MascotaCreate.as_view()), name='mascota_crear'),
    url(r'^listar', login_required(MascotaList.as_view()), name='mascota_listar'),
    url(r'^editar/(?P<pk>\d+)/$', login_required(MascotaUpdate.as_view()), name='mascota_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', login_required(MascotaDelete.as_view()), name='mascota_eliminar'),
    url(r'^listado$', listado, name='listado'),
]
