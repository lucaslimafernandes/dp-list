from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='homepage'),
    path('test/freeproxy/', view=views.vw_free_proxy, name='teste_fp'),
]