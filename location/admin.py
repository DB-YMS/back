from django.contrib import admin
from .models import Division
from .models import Site
from .models import Yard
from .models import Master

# Register your models here.
class DivisionAdmin(admin.ModelAdmin):
    search_fields = ['model']

class SiteAdmin(admin.ModelAdmin):
    search_fields = ['model']

class YardAdmin(admin.ModelAdmin):
    search_fields = ['model']

class MasterAdmin(admin.ModelAdmin):
    search_fields = ['model']

admin.site.register(Division)
admin.site.register(Site)
admin.site.register(Yard)
admin.site.register(Master)