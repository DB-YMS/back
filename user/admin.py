from django.contrib import admin
from .models import Driver

# Register your models here.
class DriverAdmin(admin.ModelAdmin):
    search_fields = ['model']

admin.site.register(Driver)