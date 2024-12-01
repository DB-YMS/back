from django.contrib import admin
from .models import Equipment

# Register your models here.
class EquipmentAdmin(admin.ModelAdmin):
    search_fields = ['model']

admin.site.register(Equipment)