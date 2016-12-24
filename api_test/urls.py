
from django.conf.urls import url,include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from teams import urls as teams_urls
from cities import urls as cities_urls
from instaTest import urls as instaTest_urls
from car import urls as car_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^team/', include(teams_urls)),
    url(r'^cities/', include(cities_urls)),
    url(r'^insta/', include(instaTest_urls)),
    url(r'^auth/', include('djoser.urls')),
    url(r'^cars/', include(car_urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),

]

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)