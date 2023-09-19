from django.shortcuts import render, redirect
from todo.models import mytodods
# Create your views here.

def mytodo(request):
    all_todo = mytodods.objects.all().order_by("-id")
    return render(request, "todo.html", {"data" : all_todo})


def savetodo(request):
    if request.method == "POST":
        titl = request.POST.get("title")
        dec = request.POST.get("dec")

        XYZ = mytodods(title = titl, desc = dec)
        XYZ.save()
        return redirect("mytodo")