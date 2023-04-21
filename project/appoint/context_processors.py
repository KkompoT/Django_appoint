from .models import Appointment



"""Считает кол-во непринятых встреч и используется для отображения в шаблоне """
def get_notification(request):
    count = Appointment.objects.filter(accepted=False).count()  # строка запрашивает у модели поле 'accepted' false
    data = {
        "count": count  # и подсчитывает
    }
    return data
