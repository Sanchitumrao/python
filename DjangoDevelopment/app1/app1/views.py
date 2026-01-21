from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Welcome to App1 Home Page")
    return render(request, 'index.html')

def about(request):
    return HttpResponse("Welcome to App1 about Page")

def contact(request):
    return HttpResponse("Welcome to App1 contact Page")