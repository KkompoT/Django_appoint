from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm

"""Форма используется для создания или обновления Appointment, включает поля модели"""
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['first_name', 'last_name', 'email', 'phone', 'request']

"""Форма отображения полей для ввода логина и пароля"""
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
