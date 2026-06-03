from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def welcome(request):
    return render(request, 'welcome.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')