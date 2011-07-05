from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

from www.sitemap import sitemaps

urlpatterns = patterns('',
    (r'^', include('frankarturo.www.urls')),
    (r'^contact/', include('frankarturo.contact_form.urls')),
    (r'^mylovelymontreal/', include('frankarturo.mylovelymontreal.urls')),

    (r'^admin/', include(admin.site.urls)),
    
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT})
    )
