from django.urls import path
from myapp import views

urlpatterns = [
    path("this", views.thisis),
    path("done", views.done),
    path("ok", views.ok),
    path("showpage", views.showthispage),
    path("newpage", views.newpage),
    path("vishal", views.vishal),

    path("", views.home),
    path("about-us", views.about),
    path("contact", views.contact, name="xyz"),


    # path("", views.myform, name = "xyz"),

    path("hit-my-data", views.savedata),

    path("delete/<int:id>", views.deletethis),
    path("update/<int:id>", views.updatethis),
    path("showupdate/<int:id>", views.showupdate),


   
]