from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def homeView(request):
    return render(request, "home.html", {})


def listEtablisView(request):
    etablissements = Etablissement.objects.all()
    return render(request, "patient/listEtablissement.html", {'etablissements': etablissements})


def detailEtablisView(request, etabli_id):
    etablis = get_object_or_404(Etablissement, pk=etabli_id)
    return render(request, "patient/detailEtablissement.html", {"etablis": etablis})


def detailRdvView(request, rendez_vous_id):
    rdv =  get_object_or_404(RendezVous, pk=rendez_vous_id)
    return render(request, "etablissement/detailRDV.html", {"item_rdv": rdv})


def ajoutEtablisView(request):
    if request.method == "POST":
        form = Etablissement_form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Etablissement_form()
        
    return render(request, "ajoutEtablissement.html", {'forms': forms})


def listRdvView(request):
    rdvs = RendezVous.objects.all()
    return render(request, "etablissement/listRDV.html", {"rdvs": rdvs})


def rendezVousView(request):
    if request.method == "POST":
        forms = RendezVous_form(request.POST)

        if forms.is_valid():
            forms.save()
    else:
        forms = RendezVous_form() 
    return render(request, "patient/createRDV.html", {'forms': forms})


def loginView(request):
    if request.method == "POST":
        form=Login_form(request.POST)
        if form.is_valid():
            matricule=form.cleaned_data.get("email")
            password=form.cleaned_data.get("password")
            user = authenticate(request, username=matricule, password=password)
            print("user authentifier")
            if user:
                if user.personnel :
                    login(request, user)
                    return redirect("ajoutEtablis")
                elif user.admin:
                    login(request, user)
                    return redirect("home")
            else:
                print("user don't exist")
        else: 
            print(form.errors)
    else: 
        form = Login_form()
    return render(request, "auth/login.html", {"form": form})


# La view pour permettre le user de se deconnecter
def logoutView(request):
    """logout logged in user"""
    logout(request)
    return redirect("login")


#La view permettant au user de se connecter
def signup_view(request):
    if request.method == "POST":
        form = User_form(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = User_form()
    
    return render(request, 'auth/signup.html', {'form': form})