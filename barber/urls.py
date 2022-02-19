from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('barbers/', views.barbers_list, name='barbers'),
    path('queryset/', views.queryset, name='queryset'),
    path('about/', views.about, name='about'),
    #path('hairstyles/', views.hairstyles, name='hairstyles'),
    path('services/', views.services, name='services'),
    path('barbers/<int:pk>/', views.barbers_details, name='barbers-detail'),
    path('services/<int:pk>/', views.service_details, name='services-detail'),
  
    #path('services/<uuid:id>/', views.service_details, name='services-detail'),
  
]
