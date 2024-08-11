from django.contrib import admin
from .models import Test

class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')

admin.site.register(Test, TestAdmin)