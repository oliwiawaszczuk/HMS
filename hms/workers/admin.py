from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Worker, WorkHours


class WorkerAdmin(UserAdmin):
    list_display = ('id', 'username',  'name', 'surname', 'profession')


admin.site.register(Worker, WorkerAdmin)


class WorkHoursAdmin(admin.ModelAdmin):
    list_display = ('id', 'worker', 'date', 'start', 'end')


admin.site.register(WorkHours, WorkHoursAdmin)

