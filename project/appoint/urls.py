from django.urls import path, include
from django.views.decorators.cache import cache_page

from appoint.views import *



urlpatterns = [
    path("", HomeTemplateView.as_view(), name="home"),
    path("make-an-appointment/", cache_page(60)(AppointmentTemplateView.as_view()), name="appointment"),  #Кеширование страницы
    path("manage-appointments/", ManageAppointmentTemplateView.as_view(), name="manage"),

    path("", include("django.contrib.auth.urls")),
    # path("register/", RegisterUserView.as_view(), name='register'),


]
