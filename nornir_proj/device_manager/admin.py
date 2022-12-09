from django.contrib import admin
from device_manager.models import Defaults

# Register your models here.
@admin.register(Defaults)
class MyModelAdmin(admin.ModelAdmin):
    # Defaults table should only have a single instance
    def has_add_permission(self, request):
        return not Defaults.objects.exists()
