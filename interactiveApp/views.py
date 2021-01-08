from django.shortcuts import render
from django.http import HttpResponse


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