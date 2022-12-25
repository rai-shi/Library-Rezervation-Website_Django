from django.urls import path
from websiteapp import views

urlpatterns = [
    path("",views.home, name="home"),
    path("home",views.home),
    path("comment",views.comment, name="comment"),
    path("communication",views.communication, name="communication"),
    path("content",views.content, name="content"),
    path("hall",views.hall, name="hall"),
    path("log_in",views.log_in, name="log_in"),
    path("sign_up",views.sign_up, name="sign_up"),
    path("profil_misafir",views.profil_misafir, name="profil_misafir"),
    path("profil_ogrenci",views.profil_ogrenci, name="profil_ogrenci"),
    path("rezervation",views.rezervation, name="rezervation"),
    path("shopping",views.shopping, name="shopping"),
]