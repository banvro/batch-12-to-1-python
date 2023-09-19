from django.urls import path
from todo import views

urlpatterns = [
    path("", views.mytodo, name="mytodo"),
    path("savetodo", views.savetodo, name="savetodo")
]