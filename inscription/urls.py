from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Page d'accueil
    path('inscrire/', views.inscrire, name='inscrire'),  # Formulaire d'inscription
    path('abonnement/', views.abonnement, name='abonnement'),  # Page d'abonnement
    path('ingenieur/', views.ingenieur, name='ingenieur'),  # Page Concours Ingénieur
    path('technicien/', views.technicien, name='technicien'),  # Page Concours Technicien
    path('master/', views.master, name='master'),  # Page Concours Master
    path('telecharger-brochure/', views.telecharger_brochure_technicien, name='telecharger_brochure'),
    path('telecharger-brochure-ingenieur/', views.telecharger_brochure_ingenieur, name='telecharger_brochure_ingenieur'),
]