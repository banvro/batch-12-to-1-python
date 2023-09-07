from django.shortcuts import render, redirect
from django.http import HttpResponse
from UsersDetail.models import StudentsInfo

# Create your views here.

def showok(request):
    return HttpResponse("this is me....")

def thisis(request):
    return HttpResponse("noooooooooo")


def showpage(request):
    return render(request, 'xyz.html')



def myform(request):
    return render(request, 'saveinfo.html')


def savedata(request):
    if request.method == 'POST':
        userid = request.POST.get('id')
        firt_name = request.POST.get('fname')
        l_name = request.POST.get('lanme')
        number = request.POST.get('phone')
        disc = request.POST.get('dec')

        savemydata = StudentsInfo(stu_id = userid, stu_f_name = firt_name, stu_l_name = l_name, phone_number = number, stu_message = disc)

        savemydata.save()

        return redirect("xyz")

        
    return HttpResponse("i am hitted....")





def first(request):
    return render(request, 'first.html')

def second(request):
    return render(request, 'second.html')