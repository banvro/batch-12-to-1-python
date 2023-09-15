from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import StudentsInfo
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
    mydata = StudentsInfo.objects.all().order_by('-id')
    print(mydata)
    return render(request, "contact.html", {"data" : mydata})


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


def deletethis(request, id):
    data = StudentsInfo.objects.get(id = id)
    data.delete()
    return redirect("xyz")
    return HttpResponse(f" i am delete {id}")

def updatethis(request, id):
    return HttpResponse(f" i am update this function {id}")

def showupdate(request):
    return HttpResponse(" i am showupdate")