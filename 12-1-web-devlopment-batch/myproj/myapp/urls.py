from django.urls import path
from myapp import views

urlpatterns = [
    path("", views.thisis),
    path("done", views.done),
    path("ok", views.ok),
    path("showpage", views.showthispage),
    path("newpage", views.newpage),
    path("vishal", views.vishal),
]