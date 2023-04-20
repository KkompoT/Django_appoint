from django.urls import path, include
from api.views import *

from rest_framework import routers

# /api/

router = routers.SimpleRouter()
router.register(r'appointment', AppointViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),   # http://127.0.0.1:8000/api/v1/Appointment/


    # path('api/v1/Appointmentlist/', AppointmentAPIList.as_view()),
    # path('api/v1/Appointmentlist/<int:pk>/', AppointmentAPIUpdate.as_view()),
    # path('api/v1/Appointmentdetail/<int:pk>/', AppintmentAPIDetailView.as_view()),

]
