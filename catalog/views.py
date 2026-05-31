from django.shortcuts import render
from .models import Well, RockSample

def index(request):
    num_wells = Well.objects.count()
    num_samples = RockSample.objects.all()
    
    context = {
        'num_wells': num_wells,
        'samples': num_samples,
    }
    return render(request, 'index.html', context)