from django.contrib import admin

from .models import *

"""Модель администратора, обеспечивает удобный интерфейс для управления объектами Appoinment,
с легким доступом к ключевым полям и опциям фильтрации"""


class AppointAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', 'sent_date', 'accepted', 'spec')
    list_display_links = ('first_name', 'id')
    search_fields = ('first_name', 'last_name')
    list_filter = ('accepted', 'sent_date')


admin.site.register(Appointment, AppointAdmin)


"""Строки настраивают заголовок и шапку интерфейса администратора"""
admin.site.site_title = 'Админка сервиса предварительной записи'
admin.site.site_header = 'Админка сервиса предварительной записи'
