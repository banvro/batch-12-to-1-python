from django.urls import path, include
from Blog import views


urlpatterns = [
    path("xyz", views.showok),
    path("abc", views.thisis),
    path("showthis", views.showpage),
    path("", views.myform, name = "xyz"),

    path("hit-my-data", views.savedata),

    path('first', views.first),
    path('second', views.second)
]
