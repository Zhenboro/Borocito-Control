from django.db import models

import uuid

# Create your models here.

class Configuration(models.Model):
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
    server_status = models.BooleanField(default=True, null=True, blank=True, verbose_name="Server Status") # if the server is online and will handle requests
    allow_new_instances = models.BooleanField(default=True, null=True, blank=True, verbose_name="¿Allow New Instances?") # if False, new Borocito-CLI instances will be blocked
    reborn_mode = models.BooleanField(default=False, null=True, blank=True, verbose_name="Reborn Mode") # allows deleted/dead Borocito-CLI instances to be handled again
    fall_back_server = models.CharField(max_length=70, null=True, blank=True, verbose_name="Fallback Server") # set a fallback server that can be used when primary is down/deleted
    key_pairs = models.JSONField(default=default_key_pairs, null=True, blank=True, verbose_name="Key Pairs")
    borocitos = models.JSONField(default=default_borocitos, null=True, blank=True, verbose_name="Borocitos")
    boro_get = models.JSONField(default=default_boro_get, null=True, blank=True, verbose_name="boro-get")
    
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return f'Configuration from {self.created_at.strftime("%d/%m/%Y, %H:%M")}. Last modified on {self.modified_at.strftime("%d/%m/%Y, %H:%M")}'

class Component(models.Model):
    name = models.CharField(max_length=70, null=True, blank=True, verbose_name="Component")
    description = models.TextField(null=True, blank=True, verbose_name="Description")
    executable = models.CharField(max_length=70, null=True, blank=True, verbose_name="Entry point")
    version = models.CharField(max_length=70, null=True, blank=True, verbose_name="Version")
    docs = models.CharField(max_length=70, null=True, blank=True, verbose_name="Documentation")
    
    binaries = models.CharField(max_length=70, null=True, blank=True, verbose_name="Binaries")
    
    author = models.CharField(max_length=70, null=True, blank=True, verbose_name="Author")
    website = models.CharField(max_length=70, null=True, blank=True, verbose_name="Website")
    
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return f'{self.name} ({self.version})'
