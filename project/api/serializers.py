from rest_framework import serializers
from appoint.models import Appointment



class AppointmentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())  # Создается скрытое поле, в этом поле прописывается текущий пользователь
    class Meta:
        model = Appointment
        fields = '__all__'