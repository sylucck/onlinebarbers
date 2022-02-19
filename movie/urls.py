from django.urls import path
from . import views

urlpatterns = [
    path('imdb/', views.home, name='home')
  
]