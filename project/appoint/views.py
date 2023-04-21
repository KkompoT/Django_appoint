from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import EmailMessage, message
from django.conf import settings
from django.contrib import messages
from .models import Appointment
from django.views.generic import ListView, TemplateView
import datetime
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.urls import reverse_lazy
from .forms import LoginUserForm, AppointmentForm
from django.core.mail import send_mail


'''Представление которое позволяет пользователям связаться 
с администраторами сайта через главную страницу по email'''
class HomeTemplateView(TemplateView):
    template_name = "appoint/index.html"

    def post(self, request):  # Почтовый запрос
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        email = EmailMessage(
            subject=f"{name} От Нас",
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_HOST_USER],
            reply_to=[email]
        )
        try:
            email.send()
            return HttpResponse("Письмо успешно отправлено")
        except Exception as a:
            return HttpResponse(f"Ошибка отправки письма: {str(a)}")



"""Представление которое содержит форму, позволяет
 пользователям отправить запрос на встречу"""
class AppointmentTemplateView(TemplateView):
    template_name = "appoint/appointment.html"

    def get(self, request, **kwargs):
        form = AppointmentForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.save()
            messages.add_message(request, messages.SUCCESS,
                                 f"Спасибо {appointment.first_name} после рассмотрения, мы ответим вам")
            return HttpResponseRedirect(request.path)

        return render(request, self.template_name, {'form': form})


'''Представлени отображает шаблон для управления встречами'''
class ManageAppointmentTemplateView(ListView):
    template_name = "appoint/manage-appointments.html"
    model = Appointment
    context_object_name = "appointments"
    login_required = True
    paginate_by = 3             # ограничение кол-ва записей , отображаемых на странице

    def post(self, request):
        date = request.POST.get("date")
        appointment_id = request.POST.get("appointment-id")
        appointment = Appointment.objects.get(id=appointment_id)
        appointment.accepted = True
        appointment.accepted_date = datetime.datetime.now()
        appointment.save()

        data = {
            "fname": appointment.first_name,
            "date": date,

        }

        message = get_template('appoint/email.html').render(data)
        email = EmailMessage(
            "О вашей записи",
            message,
            settings.EMAIL_HOST_USER,
            [appointment.email],
        )
        email.content_subtype = "html"
        email.send()

        messages.add_message(request, messages.SUCCESS, f"Вы подтвердили {appointment.first_name}")
        return HttpResponseRedirect(request.path)

    def get_context_data(self, *args, **kwargs):            # Добавляет контекст переменную title, используется для заголовка страницы
        context = super().get_context_data(*args, **kwargs)
        appointments = Appointment.objects.all()
        context.update({
            "title": "Редактор записей"
        })
        return context

    def get_queryset(self):                                 # фильтрует записи на прием , показывает только те которые не были приняты
        return Appointment.objects.all().filter(accepted=False)
