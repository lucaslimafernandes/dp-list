from django.contrib import admin
from .models import Prox, ProxyLister

# Register your models here.

admin.site.register((Prox, ProxyLister))

