from django.urls import path, include
from appoint.views import *



urlpatterns = [
    path("", HomeTemplateView.as_view(), name="home"),
    path("make-an-appointment/", AppointmentTemplateView.as_view(), name="appointment"),
    path("manage-appointments/", ManageAppointmentTemplateView.as_view(), name="manage"),

    path("", include("django.contrib.auth.urls")),
    # path("register/", RegisterUserView.as_view(), name='register'),


]
