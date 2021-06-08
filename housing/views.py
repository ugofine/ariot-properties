from django.shortcuts import render
from properties.models import Property
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    properties = Property.objects.all()
    return render(request, 'pages/index.html', {'properties': properties})

def about(request):
    properties = Property.objects.all()
    return render(request, 'pages/about.html', {'properties': properties})

def properties(request):
    properties = Property.objects.all()
    return render(request, 'pages/properties.html', {'properties': properties})

def contact(request):
    return render(request, 'pages/contact.html')

def blog(request):
    return render(request, '/blog.html')
