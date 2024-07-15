from django.http.response import HttpResponse
from django.shortcuts import render

from .models import AuthGroup, AuthGroupPermissions, AuthPermission, AuthUser, AuthUserGroups, AuthUserUserPermissions, DjangoAdminLog, DjangoContentType, DjangoMigrations, DjangoSession
from .models import Kutuphane, Misafiruye, Ogrenciuye, Oneri, Rezervasyon, Siparis, Siparisurun, Urun  
from .data import data
# Create your views here.

def home(request):
    return render(request, "websiteapp/home.html")

def comment(request):
    return render(request, "websiteapp/comment.html")

def communication(request):
    return render(request, "websiteapp/communication.html")

def content(request):
    return render(request, "websiteapp/content.html")

def hall(request):
    return render(request, "websiteapp/hall.html")

def log_in(request):
    return render(request, "websiteapp/log_in.html")

def sign_up(request):
    return render(request, "websiteapp/sign_up.html")

def profil_misafir(request):
    return render(request, "websiteapp/profil_misafir.html")

def profil_ogrenci(request):
    return render(request, "websiteapp/profil_ogrenci.html")

def rezervation(request):
    contexts = {
        "rezervations": data 
    }
    return render(request, "websiteapp/rezervation.html", data)

def shopping(request):
    return render(request, "websiteapp/shopping.html")

def myshops(request):
    return render(request, "websiteapp/myshops.html")
    
 
 
