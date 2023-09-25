from django.shortcuts import render,redirect
from django.http import HttpResponse
from todo.models import mytodods
# Create your views here.
def cars(request):
    return HttpResponse("todo world")





def webpage(request):
    all_todo = mytodods.objects.all().order_by("-id")
    return render(request, "todo.html", {"data" : all_todo, "check" : "ok"})



def update(request, x):
    all_todo = mytodods.objects.all().order_by("-id")
    my = mytodods.objects.get(id = x)
    return render(request, "todo.html", {"data" : all_todo, "check" : "checkme", "datta" : my})


def updatethis(request, x):
    my = mytodods.objects.get(id = x)
    if request.method == "POST":
        titl = request.POST.get("title")
        dec = request.POST.get("dec")

        my.title = titl
        my.desc = dec
        my.save()
        return redirect("mytodo")




def savetodo(request):
    if request.method == "POST":
        titl = request.POST.get("title")
        dec = request.POST.get("dec")
        image = request.FILES.get("img")

        XYZ = mytodods(title = titl, desc = dec, img = image)
        XYZ.save()
        return redirect("mytodo")

def deleteme(request, x):
    data = mytodods.objects.get(id = x)
    data.delete()
    return redirect("mytodo")