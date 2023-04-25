from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class Specialist(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    email = models.EmailField(max_length=50, verbose_name="Почта")
    phone = models.CharField(max_length=50, verbose_name="Телефон")
    request = models.TextField(blank=True, verbose_name="Обращение")  # Поле 'Запрос' может быть пустым
    sent_date = models.DateField(auto_now_add=True, verbose_name="Дата записи")
    accepted = models.BooleanField(default=False, verbose_name="Подтверждение")
    accepted_date = models.DateField(auto_now_add=False, null=True, blank=True, verbose_name="Назначеное время")
    spec = models.ForeignKey('Specialist', on_delete=models.CASCADE, null=True, blank=True, verbose_name="Специалист")
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True, verbose_name="Пользователь")

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ["sent_date"]  # обратный порядок сортировки
        verbose_name = "Назначение записей"
        verbose_name_plural = 'Назначение записей'
