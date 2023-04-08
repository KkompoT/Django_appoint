from django.db import models


class Appointment(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    request = models.TextField(blank=True)  # Поле 'Запрос' может быть пустым
    sent_date = models.DateField(auto_now_add=True)  # Добавление времени
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.first_name


    class Meta:
        ordering = ["-sent_date"]  # обратный порядок сортировки
