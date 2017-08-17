from django.conf.urls import url, include

from mascota.views import index_mascota, MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete

urlpatterns = [
    url(r'^$', index_mascota, name='index_mascota'),
    url(r'^nuevo$', MascotaCreate.as_view(), name='mascota_crear'),
    url(r'^listar$', MascotaList.as_view(), name='mascota_listar'),
    url(r'^editar/(?P<pk>\d+)/$', MascotaUpdate.as_view(), name='mascota_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', MascotaDelete.as_view(), name='mascota_eliminar'),

]
