from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^edutime/', include('edutime.urls', namespace="edutime")),
    url(r'^getit/', include('getit.urls', namespace="getit")),
    url(r'^admin/', include(admin.site.urls))
]