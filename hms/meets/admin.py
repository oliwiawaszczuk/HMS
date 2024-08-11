from django.contrib import admin
from .models import Meet


class MeetAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'start', 'end')
    filter_horizontal = ('workers',)

admin.site.register(Meet)
