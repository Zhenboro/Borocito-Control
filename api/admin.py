from django.contrib import admin

# Register your models here.
from api.models import Instancia, Telemetria

class InstanciaAdmin(admin.ModelAdmin):
    list_display = ["uuid", "username", "ver_usuario_dominio", "windows", "created_at"]
    list_filter = ["created_at", "windows", "key", "domain"]
    ordering = ["-created_at"]
    search_fields = ["uuid", "username"]
    
    @admin.display(empty_value="???", description="Usuario @ Dominio")
    def ver_usuario_dominio(self, obj):
        return f'{obj.username} @ {obj.domain}'

class TelemetriaAdmin(admin.ModelAdmin):
    list_display = ["uuid", "filename", "size", "instance", "created_at"]
    list_filter = ["created_at", "extension"]
    ordering = ["-created_at"]
    search_fields = ["uuid", "filename"]

admin.site.register(Instancia, InstanciaAdmin)
admin.site.register(Telemetria, TelemetriaAdmin)
