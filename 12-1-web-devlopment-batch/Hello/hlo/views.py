from django.shortcuts import render
from django.http import HttpResponse
from hlo.models import ContactUs
# Create your views here.


def car(request):
    return HttpResponse("ok")

def showupdate(request, x):
    xyz = ContactUs.objects.get(id = x)
    # xyz.delete()
    return render(request, 'thisfile.html', {"abc" : xyz})