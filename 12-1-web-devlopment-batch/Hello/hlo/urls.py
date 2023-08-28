from django.urls import path, include
from hlo import views

urlpatterns = [
    path('car', views.car),
    path('mypage', views.showthis)
]  