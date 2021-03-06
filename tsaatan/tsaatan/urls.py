from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404

handler404 = "website.views.view_404"

urlpatterns = [
    path('', include('website.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns = urlpatterns + \
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
