from django.db import models
from django.utils import timezone

# Create your models here.



class Prox(models.Model):

    lister = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=39, unique=True)
    port = models.IntegerField()
    protocol = models.CharField(max_length=20) 
    country = models.CharField(max_length=30)
    latency = models.CharField(max_length=10)
    requests = models.IntegerField(default=0)
    status_ok = models.IntegerField(default=0)


class ProxyLister(models.Model):

    url = models.CharField(max_length=200)
    dt_include = models.DateTimeField(auto_now=True)
    
