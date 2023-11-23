from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    return render(request, 'nuestrapp/base.html')