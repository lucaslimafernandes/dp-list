from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='homepage'),
    path('get/', views.list_proxies, name='list_proxies'),
    path('test/freeproxy/', view=views.vw_free_proxy, name='teste_fp'),
]