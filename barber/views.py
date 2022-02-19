from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
# Create your views here.


def home(request):
    return render(request, 'home.html')

def queryset(request):
    all_barbers = Barber.objects.all()
    all_hairstyles = Skill.objects.all()
    all_services= Service.objects.all()
    num_barbers = Barber.objects.all().count()
    num_available = Service.objects.filter(status='0').count()
    num_working = Service.objects.filter(status='1').count()
    num_unavailable = Service.objects.filter(status='2').count()
    available = Service.objects.filter(status='0')
    working = Service.objects.filter(status='1')
    unavailable = Service.objects.filter(status='2')

    context = {
        'all_barbers': all_barbers,
        'all_hairstyles': all_hairstyles,
        'all_services': all_services,
        'num_barbers': num_barbers,
        'num_avaliable':num_available,
        'num_working':num_working,
        'num_unavailable':num_unavailable,
        'available':available ,
        'working': working,
        'unavailable':  unavailable,
    }

    return render(request, 'queryset.html', context)

def barbers_list(request):
    barbers = Barber.objects.all()

    context = {
        'barbers': barbers,
    }
    return render(request, 'barbers_list.html', context)



def services(request):

    services = Service.objects.all()

    context={
        'services':services
    }

    return render(request, 'services.html', context)

def barbers_details(request, pk):

    barb = get_object_or_404(Barber, pk=pk)

    context = {
        'barb': barb,
    }
    return render(request, 'barbers_details.html', context)

def service_details(request, pk):

    serve = get_object_or_404(Service, pk=pk)

    context = {
        'serve': serve,
    }
    return render(request, 'service_details.html', context)

def about(request):
    abouts = About.objects.all()
    
    return render(request, 'about.html', {'abouts': abouts,})