from django.shortcuts import render
from .forms import CandidatForm

# Vue pour l'inscription
def inscrire(request):
    if request.method == 'POST':
        form = CandidatForm(request.POST, request.FILES)
        if form.is_valid():
            candidat = form.save()
            return render(request, 'inscription/recu.html', {'candidat': candidat})
    else:
        form = CandidatForm()
    return render(request, 'inscription/formulaire.html', {'form': form})

# Vue pour la page d'accueil
def home(request):
    return render(request, 'inscription/home.html')

# Vue pour l’abonnement
def abonnement(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        nom = request.POST.get('nom')
        prenoms = request.POST.get('prenoms')
        etablissement = request.POST.get('etablissement')
        niveau = request.POST.get('niveau')
        return render(request, 'inscription/merci_abonnement.html', {'nom': nom})
    
    return render(request, 'inscription/abonnement.html')

# Vue "En savoir plus" - Concours Ingénieur
def ingenieur(request):
    return render(request, 'inscription/ingenieur.html')

# Vue "En savoir plus" - Concours Technicien
def technicien(request):
    return render(request, 'inscription/technicien.html')

# Vue "En savoir plus" - Concours Master
def master(request):
    return render(request, 'inscription/master.html')
