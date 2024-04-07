from django.shortcuts import render, redirect, get_object_or_404
from .models import Aplicatie, Endpoint, Bug, SetariUtilizator
from .forms import AplicatieForm, EndpointForm, UserForm, BugForm, SetariForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
import datetime
import requests

def home(request):
    date = datetime.datetime.now().year
    model = Aplicatie.objects.all()
    context = {
        'date':date,
        'model':model
    }
    return render(request, "my_app/home.html", context)

#################################################
####################AUTH#########################
#################################################

def inregistrare_user(request):
    date = datetime.datetime.now().year
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my_app:login_user')
        else:
            form = UserForm()
            messages.info(request, "Error!")
    context = {
        'form':form,
        'date':date
    }
    return render(request, 'my_app/inregistrare_user.html', context)

def login_user(request):
    date_posted = datetime.datetime.now().year
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("account")
        else:
            messages.info(request, "Error!")
    context = {
        'date_posted':date_posted,
    }
    return render(request, "my_app/login_user.html", context)

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))

############################################
############CRUD############################
############################################

@login_required
def account(request):
    user = request.user
    model1 = user.aplicatie_set.all()
    model2 = user.endpoint_set.all()
    context = {
        'model1':model1,
        'model2':model2,
    }
    return render(request, "my_app/account.html", context)

@login_required
def register_app(request):
    date = datetime.datetime.now().year
    form = AplicatieForm()
    if request.method == "POST":
        form = AplicatieForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = AplicatieForm()
            messages.info(request, "Error")
    context = {
        'date':date,
        'form': form,
    }
    return render(request, "my_app/register_app.html", context)

@login_required
def register_endpoint(request, pk):
    date = datetime.datetime.now().year
    form = EndpointForm()
    model1 = Aplicatie.objects.get(id=pk)
    if request.method == "POST":
        form = EndpointForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = EndpointForm()
            messages.info(request, "Error")
    context = {
        'date':date,
        'form':form,
        'model1':model1,
    }
    return render(request, "my_app/register_endpoint.html", context)

def raportare_bug(request, pk):
    form = BugForm()
    model = Aplicatie.objects.get(id=pk)
    a_model = Aplicatie.objects.filter(id=pk)
    model2 = User.objects.filter(id=pk)
    if request.method == 'POST':
        form = BugForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = BugForm()
    context = {
        'form':form,
        'model':model,
        'a_model':a_model,
        'model2':model2,
    }
    return render(request, "my_app/raportare_bug.html", context)

@login_required
def dashboard_dezvoltator(request):
    user = request.user
    model = user.bug_set.all()
    verificare = True
    context = {
        'model':model,
        'verificare':verificare,
    }
    return render(request, 'my_app/dashboard_dev.html', context)

@login_required
def status(request, pk):
    model = Endpoint.objects.get(id=pk)
    date = datetime.datetime.now()
    try:
        response = requests.get(model.url, timeout=10)
        if response.status_code >= 200 and response.status_code <= 302:
            status = 'Stable'
        else:
            status = 'Unstable'

    except requests.exceptions.RequestException as e:
        status = 'Down'
    
    setari, created = SetariUtilizator.objects.get_or_create(utilizator=request.user)
    
    if request.method == 'POST':
        form = SetariForm(request.POST, instance=setari)
        if form.is_valid():
            form.save()
            return redirect('status')
    else:
        form = SetariForm(instance=setari)

    context = {'endpoint': model, 'status': status, 'form':form, 'date':date}
    return render(request, "my_app/status.html", context)

#########################################
#################TIER4###################
#########################################

##########################################
#################TIER5####################
##########################################

def editare_setari(request):
    if request.method == 'POST':
        form = SetariForm(request.POST, instance=request.user.setari)
        if form.is_valid():
            form.save()
            return JsonResponse({"mesaj": "Setările au fost actualizate cu succes!"})
        else:
            return JsonResponse({"erori": form.errors}, status=400)

# Create your views here.
