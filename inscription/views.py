from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from io import BytesIO
from xhtml2pdf import pisa
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

# Vue pour l'abonnement
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

# Vue "brochure" - concours technicien
def telecharger_brochure_technicien(request):
    """Génère et télécharge la brochure au format PDF avec xhtml2pdf"""
    
    context = {
        'titre': 'Concours Technicien',
        'sous_titre': 'Pour les titulaires du BAC',
    }
    
    # Rendre le template
    html_string = render_to_string('inscription/brochure_technicien_pdf.html', context)
    
    # Générer le PDF avec xhtml2pdf
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html_string.encode("UTF-8")), dest=result)
    
    if not pdf.err:
        response = HttpResponse(result.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Brochure_Concours_Technicien_ESATIC.pdf"'
        return response
    else:
        return HttpResponse("Erreur lors de la génération du PDF")
    # Vue pour télécharger la brochure Ingénieur
def telecharger_brochure_ingenieur(request):
    context = {
        'titre': 'Concours Ingénieur',
        'sous_titre': 'Pour les titulaires d\'un BAC+2 minimum',
    }
    
    html_string = render_to_string('inscription/brochure_ingenieur_pdf.html', context)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html_string.encode("UTF-8")), dest=result)
    
    if not pdf.err:
        response = HttpResponse(result.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Brochure_Concours_Ingenieur_ESATIC.pdf"'
        return response
    else:
        return HttpResponse("Erreur lors de la génération du PDF")
