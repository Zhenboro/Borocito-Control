from django.contrib import admin

# Register your models here.
from configs.models import Configuration, Component

admin.site.register(Configuration)
admin.site.register(Component)
