from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from api.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from api.serializers import AppointmentSerializer
from appoint.models import Appointment, Specialist


# class AppointViewSet(viewsets.ModelViewSet):
#     queryset = Appointment.objects.all()
#     serializer_class = AppointmentSerializer



class AppointmentAPIList(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class AppointmentAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = (IsOwnerOrReadOnly, )

class AppintmentAPIDetailView(generics.RetrieveDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = (IsAdminOrReadOnly,)
