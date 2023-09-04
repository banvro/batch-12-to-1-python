from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def showok(request):
    return HttpResponse("this is me....")

def thisis(request):
    return HttpResponse("noooooooooo")


def showpage(request):
    return render(request, 'xyz.html')



def myform(request):
    return render(request, 'saveinfo.html')