from django.urls import path
from.import views

urlpatterns = [
    path('', views.home),
    path('home', views.home),
    path('communication', views.communication),
    path('about-us', views.aboutUs),
]
