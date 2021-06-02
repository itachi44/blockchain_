from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import *
from django.db import transaction, IntegrityError

#page d'accueil
def index(request):
    name="bamba"
    context = {
        'name':name
        
    }
    return render(request, 'blockchainApp/index.html', context)


def dashboard(request):
    context={

        }
    return render(request, 'blockchainApp/dashboard.html', context)
