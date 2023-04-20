from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.serializers import AppointmentSerializer
from appoint.models import Appointment, Specialist


class AppointViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer



# class AppointmentAPIList(generics.ListCreateAPIView):
#     queryset = Appointment.objects.all()
#     serializer_class = AppointmentSerializer
#
#
# class AppointmentAPIUpdate(generics.UpdateAPIView):
#     queryset = Appointment.objects.all()
#     serializer_class = AppointmentSerializer
#
#
# class AppintmentAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Appointment.objects.all()
#     serializer_class = AppointmentSerializer
