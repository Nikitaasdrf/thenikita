from django.urls import path, include
from . import views

urlpatterns = [
    path('next/', views.next, name='next'),
    path('registration/', views.registration, name='registration'),
    path('logout/', views.Ryzhovlogout, name='Ryzhovlogout'),
]