from django.db import models

import uuid

# Create your models here.

class Configuration(models.Model):
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Configuration"
        verbose_name_plural = "Configurations"
    def default_key_pairs() -> list:
        return [ # these are the keys Borocito-CLI uses to make requests to this server
            str(uuid.uuid4()),
            str(uuid.uuid4()),
            str(uuid.uuid4()),
        ]
    def default_borocitos() -> dict:
        return { # this is where Borocito-Updater can get version and binaries to download and update
            "version": "0.3.0.0",
            "binaries": "/Borocitos.zip",
        }
    def default_boro_get() -> dict:
        return { # the boro-get component will request this information for component manage
            "version": "1.2.0.0",
            "binary": "/boro-get/boro-get.zip",
            "repository": "/boro-get/repository.ini",
        }
    server_status = models.BooleanField(default=True, null=True, blank=True, verbose_name="Server Status", help_text="Allow server to handle all requests.")
    allow_new_instances = models.BooleanField(default=True, null=True, blank=True, verbose_name="¿Allow New Instances?", help_text="Allow new Borocito-CLI report instances to be handled.")
    reborn_mode = models.BooleanField(default=False, null=True, blank=True, verbose_name="Reborn Mode", help_text="Allows old/deleted instances to be handled again.")
    fall_back_server = models.CharField(max_length=70, null=True, blank=True, verbose_name="Fallback Server", help_text="Set a fallback server that can be used when Primary is down/offline.")
    key_pairs = models.JSONField(default=default_key_pairs, null=True, blank=True, verbose_name="Key Pairs", help_text="The Key-Pairs instances need to make requests.")
    borocitos = models.JSONField(default=default_borocitos, null=True, blank=True, verbose_name="Borocitos", help_text="For Borocito-Updater to search and download updates.")
    boro_get = models.JSONField(default=default_boro_get, null=True, blank=True, verbose_name="boro-get", help_text="boro-get and Borocito-CLI will need this information.")
    
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return f'Configuration from {self.created_at.strftime("%d/%m/%Y, %H:%M")}. Last modified on {self.modified_at.strftime("%d/%m/%Y, %H:%M")}'

class Component(models.Model):
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Component"
        verbose_name_plural = "Components"
    name = models.CharField(max_length=70, null=True, blank=True, verbose_name="Component", help_text="Component name.")
    description = models.TextField(null=True, blank=True, verbose_name="Description", help_text="Short description.")
    executable = models.CharField(max_length=70, null=True, blank=True, verbose_name="Entry point", help_text="Executable file to run for when is used/installed.")
    version = models.CharField(max_length=70, null=True, blank=True, verbose_name="Version", help_text="Version of the component.")
    docs = models.CharField(max_length=70, null=True, blank=True, verbose_name="Documentation", help_text="Where you can find useful information about this component.")
    
    binaries = models.CharField(max_length=70, null=True, blank=True, verbose_name="Binaries", help_text="From where will boro-get get this component.")
    
    author = models.CharField(max_length=70, null=True, blank=True, verbose_name="Author")
    website = models.CharField(max_length=70, null=True, blank=True, verbose_name="Website")
    
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return f'{self.name} ({self.version})'
