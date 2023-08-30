from django.urls import path, include
from Blog import views


urlpatterns = [
    path("", views.showok),
    path("abc", views.thisis),
    path("showthis", views.showpage)
]
