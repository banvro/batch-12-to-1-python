from django.urls import path
from todo import views

urlpatterns = [
    path('first',views.cars),
    path('',views.webpage,name="mytodo"),
    path("savetodo", views.savetodo, name="savetodo"),
    
    path("deletethis/<int:x>", views.deleteme),
    
    path("update/<int:x>", views.update),
    path("updatethis/<int:x>", views.updatethis),
]

