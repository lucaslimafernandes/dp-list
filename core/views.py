from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import Prox, ProxyLister
from .forms import ProxForm

from datetime import date, datetime
from .scrap.free_proxy import get_free_proxy



from django.shortcuts import render

# Create your views here.


def home(request):
    return HttpResponse('Hello World!')


def list_proxies(request):

    lp = ProxyLister.objects.all().values_list(named=True)



    return HttpResponse(lp)





def vw_free_proxy(request):

    data = get_free_proxy()

    for i in data:

        p = ProxForm(i)
        if p.is_valid():
            new_p = p.save()



    return HttpResponse(data)
    

