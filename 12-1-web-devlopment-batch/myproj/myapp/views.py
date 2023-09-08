from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def thisis(request):
    print("wwwwwwwwwwwwwwwwwwwww")
    return HttpResponse("i am a good devloper...")


def done(request):
    return HttpResponse("i am from done url...")


def ok(request):
    return HttpResponse("i am from ok url...")


def showthispage(request):
    return render(request, 'xyz.html')


def newpage(request):
    return render(request, 'abc.html')

def vishal(request):
    return render(request, 'new.html')


def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")
