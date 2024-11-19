from django.contrib import admin
from .models import Equipment
from .models import Yard
from .models import Site
from .models import Master
from .models import Transaction
from .models import Driver
from .models import Division

# Register your models here.
class EquipmentAdmin(admin.ModelAdmin):
    search_fields = ['model']

class YardAdmin(admin.ModelAdmin):
    search_fields = ['model']

class SiteAdmin(admin.ModelAdmin):
    search_fields = ['model']

class MasterAdmin(admin.ModelAdmin):
    search_fields = ['model']

class TransactionAdmin(admin.ModelAdmin):
    search_fields = ['model']

class DriverAdmin(admin.ModelAdmin):
    search_fields = ['model']

class DivisionAdmin(admin.ModelAdmin):
    search_fields = ['model']

admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Yard, YardAdmin)
admin.site.register(Site, SiteAdmin)
admin.site.register(Master, MasterAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Division, DivisionAdmin)