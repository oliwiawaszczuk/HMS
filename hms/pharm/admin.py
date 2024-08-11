from django.contrib import admin
from .models import Drug

class DrugAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'expiration_date')

admin.site.register(Drug, DrugAdmin)
