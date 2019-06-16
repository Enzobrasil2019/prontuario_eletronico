from django.shortcuts import render
from django.utils import timezone
from .models import Medico

# Create your views here.

def post_list(request): 
    Medicos = Medico.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'medicos/post_list.html', {'Medicos': Medicos})
# Create your views here.
