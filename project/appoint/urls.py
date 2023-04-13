from django.urls import path
from appoint.views import *

urlpatterns = [
    path("", HomeTemplateView.as_view(), name="home"),
    path("make-an-appointment/", AppointmentTemplateView.as_view(), name="appointment"),
    path("manage-appointments/", ManageAppointmentTemplateView.as_view(), name="manage"),
    # path("register/", RegisterUserView.as_view(), name='register'),
    path("login/", login, name='login')

]
