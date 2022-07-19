"""
    Meer_Balaj_CV URL Configuration

"""


from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url
from django.views.static import serve


urlpatterns = [

    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('spam/', admin.site.urls),
    path('', include("meerbalajcv.urls")),
    path('', include('pwa.urls')),
    
    path('accounts/', include("registration.backends.default.urls")),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Meer Balaj Admin Portal"
admin.site.site_title = "Meer Balaj Admin Portal"
admin.site.index_title = "Welcome to Meer Balaj CV Admin Portal"