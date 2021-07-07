from django.shortcuts import render
from .models import Destinations

# Create your views here.
def home(request):
    dests = Destinations.objects.all()
    return render(request, 'home.html',  {'dests': dests})

def about(request):
    return render(request, 'about.html')

def news(request):
    return render(request, 'news.html')

def contact(request):
    return render(request, 'contact.html')

def destinations(request):
    return render(request, 'destinations.html')
