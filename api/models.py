from django.db import models

import uuid

# Create your models here.

class Instancia(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    key = models.CharField(max_length=70, null=True, blank=True) # api key used to create the instance. REVIEW
    borocito = models.CharField(max_length=70, null=True, blank=True)
    username = models.CharField(max_length=70, null=True, blank=True)
    domain = models.CharField(max_length=70, null=True, blank=True)
    local_ip = models.GenericIPAddressField(null=True, blank=True)
    public_ip = models.GenericIPAddressField(null=True, blank=True)
    language = models.CharField(max_length=70, null=True, blank=True)
    windows = models.CharField(max_length=70, null=True, blank=True)
    ram = models.CharField(max_length=70, null=True, blank=True)
    screen = models.CharField(max_length=90, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return f'[{self.uuid}] {self.username} at {self.domain} on {self.windows}'

    def nombre(self):
        return f'[{self.uuid}] {self.username} at {self.domain}'
