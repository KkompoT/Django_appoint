from rest_framework import serializers
from appoint.models import Appointment


"""Класс сериализатора, определяет как модель Appoinment
 должна быть сериализована в JSON-представление
  для использования в ответах API"""
class AppointmentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault())  # Создается скрытое поле, в этом поле прописывается текущий пользователь

    class Meta:
        model = Appointment
        fields = '__all__'
