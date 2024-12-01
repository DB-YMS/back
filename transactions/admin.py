from django.contrib import admin
from .models import Transaction

# Register your models here.
class TransactionAdmin(admin.ModelAdmin):
    search_fields = ['model']

admin.site.register(Transaction)