from django.contrib import admin
from .models import Patient

class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'age', 'gender', 'birthday')

admin.site.register(Patient, PatientAdmin)