from django.contrib import admin

# Register your models here.
from configs.models import Configuration, Component

class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ["__str__", "created_at", "modified_at"]
    list_filter = ["created_at", "key_pairs"]
    ordering = ["-created_at"]

class ComponentAdmin(admin.ModelAdmin):
    list_display = ["name", "version",  "created_at"]
    list_filter = ["created_at", "version", "author"]
    ordering = ["-created_at"]
    search_fields = ["name"]


admin.site.register(Configuration, ConfigurationAdmin)
admin.site.register(Component, ComponentAdmin)
