
from django.contrib import admin
from django.urls import path, include

from appoint.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appoint.urls'))

]
