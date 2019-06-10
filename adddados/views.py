from django.shortcuts import render
from django.utils import timezone
from .models import Pacientes

# Create your views here.
def post_list(request): 

    return render(request, 'adddados/post_list.html', {'posts':Pacientes})