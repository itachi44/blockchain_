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


#page connexion admin
def dashboard_login(request):
    context={

        }
    return render(request, 'blockchainApp/dashConnexion.html', context)

#page admin
def dashboard_admin(request):
    context={

        }
    return render(request, 'blockchainApp/dashboard.html', context)

#page proprietaire
def property_owner(request):
    context={

        }
    return render(request, 'blockchainApp/proprietaire.html', context)
