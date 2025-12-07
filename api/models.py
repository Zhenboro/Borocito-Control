from django.db import models

import uuid

# Create your models here.

class Instancia(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="UUID", help_text="Unique identificator for the instance.")
    key = models.CharField(max_length=70, null=True, blank=True, verbose_name="Key-Pair", help_text="Key-Pair used to make requests.")
    borocito = models.CharField(max_length=70, null=True, blank=True, verbose_name="Borocito", help_text="Borocito instance information.")
    username = models.CharField(max_length=70, null=True, blank=True, verbose_name="User name", help_text="Windows user name account.")
    domain = models.CharField(max_length=70, null=True, blank=True, verbose_name="Domain", help_text="Windows domain name.")
    local_ip = models.GenericIPAddressField(null=True, blank=True, verbose_name="Local IP", help_text="Local network IP.")
    public_ip = models.GenericIPAddressField(null=True, blank=True, verbose_name="Public IP", help_text="Public network IP.")
    language = models.CharField(max_length=70, null=True, blank=True, verbose_name="Language", help_text="Windows language.")
    windows = models.CharField(max_length=70, null=True, blank=True, verbose_name="Windows", help_text="Windows information.")
    ram = models.CharField(max_length=70, null=True, blank=True, verbose_name="RAM", help_text="RAM available.")
    screen = models.CharField(max_length=90, null=True, blank=True, verbose_name="Screen", help_text="Screen information.")
    
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return f'[{self.uuid}] {self.username} at {self.domain} on {self.windows}'

    def nombre(self):
        return f'[{self.uuid}] {self.username} at {self.domain}'
