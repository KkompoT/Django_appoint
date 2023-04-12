from django.contrib import admin

from .models import *


class AppointAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', 'sent_date', 'accepted',)
    list_display_links = ('first_name', 'id')
    search_fields = ('first_name', 'last_name')
    list_filter = ('accepted', 'sent_date')


admin.site.register(Appointment, AppointAdmin)
