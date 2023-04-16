from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from project import settings

from appoint.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appoint.urls'))

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

