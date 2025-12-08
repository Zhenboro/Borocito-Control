from django.db import models
from django.conf import settings

import uuid
import os

# Create your models here.

class Instancia(models.Model):
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Instancia"
        verbose_name_plural = "Instancias"
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="UUID", help_text="Unique identificator for the instance.")
    key = models.CharField(max_length=70, null=True, blank=True, verbose_name="Key-Pair", help_text="Key-Pair used to make requests.")
    borocito = models.CharField(max_length=70, null=True, blank=True, verbose_name="Borocito", help_text="Borocito instance information.")
    username = models.CharField(max_length=70, null=True, blank=True, verbose_name="User name", help_text="Windows user name account.")
    domain = models.CharField(max_length=70, null=True, blank=True, verbose_name="Domain", help_text="Windows domain name.")
    local_ip = models.GenericIPAddressField(null=True, blank=True, verbose_name="Local IP", help_text="Local network IP.")
    public_ip = models.GenericIPAddressField(null=True, blank=True, verbose_name="Public IP", help_text="Public network IP.")
    language = models.CharField(max_length=70, null=True, blank=True, verbose_name="Language", help_text="Windows language.")
    windows = models.CharField(max_length=70, null=True, blank=True, verbose_name="Windows", help_text="Windows information.")
    ram = models.CharField(max_length=70, null=True, blank=True, verbose_name="RAM", help_text="RAM available in bytes.")
    screen = models.CharField(max_length=90, null=True, blank=True, verbose_name="Screen", help_text="Screen information.")
    
    command = models.TextField(null=True, blank=True, verbose_name="Command", help_text="IDFTP command.")
    response = models.TextField(null=True, blank=True, verbose_name="Response", help_text="IDFTP command response.")
    
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return f'[{self.uuid}] {self.username} at {self.domain}'

    def nombre(self):
        return f'[{self.uuid}] {self.username} at {self.domain}'

class Telemetria(models.Model):
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Telemetria"
        verbose_name_plural = "Telemetrias"
    def telemetry_file_path(instance, filename):
        return os.path.join(settings.BOROCITO_TELEMETRY_DIR, str(instance.uuid))
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="UUID", help_text="Unique identificator.")
    filename = models.CharField(max_length=100, null=True, blank=True, verbose_name="File name", help_text="Full file name.")
    extension = models.CharField(max_length=6, null=True, blank=True, verbose_name="Format", help_text="File extension.")
    size = models.PositiveIntegerField(null=True, blank=True, verbose_name="Size", help_text="File size in KB.")
    instance = models.ForeignKey(Instancia, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Instance", help_text="Borocito-CLI instance.")
    telemetry = models.FileField(upload_to=telemetry_file_path, verbose_name="File", help_text="The actual file.")
    
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return f'[{self.uuid}] \'{self.filename}\' uploaded by {self.instance} on {self.created_at}'
