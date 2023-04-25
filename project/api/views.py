from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from api.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from api.serializers import AppointmentSerializer
from appoint.models import Appointment

""""Класс представления , который позволяет авторизованному пользователю
 получать список объектов и создавать их:  Appointment"""


class AppointmentAPIList(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # authentication_classes = (TokenAuthentication,)


""""Класс представления , который позволяет авторизованному пользователю
 получать и обновлять объект Appointment"""


class AppointmentAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    # authentication_classes = (TokenAuthentication,)


""""Класс представления , который позволяет пользователю Администратору
 получать и удалять объекты Appointment, ограничивает при этом доступ 
 для других пользователей"""


class AppointmentAPIDetailView(generics.RetrieveDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = (IsAdminOrReadOnly,)
    # authentication_classes = (TokenAuthentication, )
