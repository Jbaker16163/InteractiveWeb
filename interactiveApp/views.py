from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
adventureData = {}

def home_page(request):
    adventureData['aName'] = request.POST.get('adventureName', None)
    
    return render(request, 'home.html', adventureData)
def first_page(request):
    adventureData['aClass'] = request.POST.get('classForm', None)

    return render(request, 'firstInteractive.html', adventureData)
def second_page(request):
    adventureData['aRace'] = request.POST.get('raceForm', None)
    
    return render(request, 'secondInteractive.html', adventureData)
def third_page(request):
    return render(request, 'thirdInteractive.html', adventureData)
def fourth_page(request):
    adventureData['aLocation'] = request.POST.get('location', None)

    return render(request, 'fourthInteractive.html', adventureData)
def fifth_page(request):
    return render(request, 'fifthInteractive.html', adventureData)

def sixth_page(request):
    return render(request, 'sixthInteractive.html', adventureData)

def register(response):
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()

    return render(response, "register/register.html", {"form":form})