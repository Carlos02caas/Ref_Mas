from django.conf.urls import url, include

from mascota.views import index_mascota

urlpatterns = [
    url(r'^$', index_mascota),
]
