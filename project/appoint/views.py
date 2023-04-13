from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import EmailMessage, message
from django.conf import settings
from django.contrib import messages
from .models import Appointment
from django.views.generic import ListView, FormView, TemplateView
import datetime
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from django.core.mail import send_mail


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


class AppointmentTemplateView(TemplateView):
    template_name = "appoint/appointment.html"

    def post(self, request):
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        message = request.POST.get("request")

        appointment = Appointment.objects.create(
            first_name=fname,
            last_name=lname,
            email=email,
            phone=mobile,
            request=message,
        )

        appointment.save()

        messages.add_message(request, messages.SUCCESS, f"Спасибо {fname} после рассмотрения, мы ответим вам")
        return HttpResponseRedirect(request.path)


class ManageAppointmentTemplateView(ListView):
    template_name = "appoint/manage-appointments.html"
    model = Appointment
    context_object_name = "appointments"
    login_required = True
    paginate_by = 3

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

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        appointments = Appointment.objects.all()
        context.update({
            "title": "Редактор записей"
        })
        return context


# class RegisterUserView(FormView):
#     template_name = 'appoint/register.html'
#     form_class = UserCreationForm
#     success_url = reverse_lazy('home')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = "Регистрация"
#         return context
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


def login(request):
    return HttpResponse
