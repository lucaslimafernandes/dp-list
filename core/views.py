from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import date, datetime
from django.contrib.auth.hashers import make_password



from django.shortcuts import render

# Create your views here.


def home(request):
    return HttpResponse('Hello World!')


