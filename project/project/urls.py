
from django.contrib import admin
from django.urls import path, include

from appoint.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('appoint', index)

]
