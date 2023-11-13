from django import forms
from .models import Prox, ProxyLister
from django.contrib.auth import get_user_model
#from django.contrib.auth.forms import UserCreationForm




class ProxForm(forms.ModelForm):
    # description = forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows': 2}))
    class Meta:

        model = Prox
        fields = ['ip_address', 'port', 'protocol', 'country', 'latency']





