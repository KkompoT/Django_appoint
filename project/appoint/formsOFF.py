from django import forms
from .models import *

class AppointmentForm(forms.Form):
    fname = forms.CharField(max_length=100, label="Имя*", widget=forms.TextInput(attrs={'placeholder': 'Введите свое имя'}))
    lname = forms.CharField(max_length=100, label="Фамилия*", widget=forms.TextInput(attrs={'placeholder': 'Введите свою фамилию'}))
    email = forms.EmailField(label="Ваш Email*", widget=forms.TextInput(attrs={'placeholder': ''}))
    mobile = forms.CharField(max_length=20, label="Номер телефона*", widget=forms.TextInput(attrs={'placeholder': ''}))
    request = forms.CharField(max_length=1000, label="Опишите кратко по какому поводу обращаетесь и с вами свяжутся*", widget=forms.Textarea(attrs={'placeholder': ''}))
    # def save(self, commit=True):
    #     appointment = super().save(commit=False)
    #     if commit:
    #         appointment.save()
    #     return appointment
    # choice = forms.ModelChoiceField(queryset=Specialist.objects.all())