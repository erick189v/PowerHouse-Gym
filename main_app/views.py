from django.shortcuts import render

from .models import Journey

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def journey_index(request):
    journey = Journey.objects.all()#retriveves all journey exercises
    return render(request, 'index.html',{
        'journeys': journey
    })

def journey_detail(request,journey_id):
    journey = Journey.objects.get(id=journey_id)
    return render(request, 'journeys/details.html', {'journey':journey})