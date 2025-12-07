from django.contrib import admin

# Register your models here.
from api.models import Instancia

class InstanciaAdmin(admin.ModelAdmin):
    list_display = ["uuid", "username", "ver_usuario_dominio", "windows", "created_at"]
    list_filter = ["created_at", "windows", "key", "domain"]
    ordering = ["-created_at"]
    search_fields = ["uuid", "username"]
    
    @admin.display(empty_value="???", description="Usuario @ Dominio")
    def ver_usuario_dominio(self, obj):
        return f'{obj.username} @ {obj.domain}'

admin.site.register(Instancia, InstanciaAdmin)
