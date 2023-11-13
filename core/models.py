from django.db import models
from django.utils import timezone

# Create your models here.



class Prox(models.Model):

    lister = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=39)
    port = models.IntegerField()
    protocol = models.CharField(max_length=20) 
    country = models.CharField(max_length=30)
    latency = models.CharField(max_length=10)
    request = models.IntegerField()
    status_ok = models.IntegerField()


class ProxyLister(models.Model):

    url = models.CharField(max_length=200)
    
