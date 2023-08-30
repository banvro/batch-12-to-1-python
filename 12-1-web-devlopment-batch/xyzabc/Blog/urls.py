from django.urls import path, include
from Blog import views


urlpatterns = [
    path("xyz", views.showok)
]
