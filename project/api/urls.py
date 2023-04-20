from django.urls import path, include, re_path
from api.views import *

from rest_framework import routers

# /api/

# router = routers.SimpleRouter()
# router.register(r'appointment', AppointViewSet)

urlpatterns = [
    # path('api/v1/', include(router.urls)),   # http://127.0.0.1:8000/api/v1/Appointment/
    path('api/v1/drf-auth/', include('rest_framework.urls')),   # Авторизация с помощью кук
    path('api/v1/appointment/', AppointmentAPIList.as_view()),
    path('api/v1/appointment/<int:pk>/', AppointmentAPIUpdate.as_view()),
    path('api/v1/appointmentdetail/<int:pk>/', AppintmentAPIDetailView.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),   # авторизация по токенам

]
