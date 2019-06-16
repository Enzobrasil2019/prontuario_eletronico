from django.shortcuts import render
from django.utils import timezone
from .models import Ambulatorio
from .forms import PostForm
# Create your views here.

def post_list(request): 
    Ambulatorios = Ambulatorio.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'mostambulatorial/mostamb.html', {'Ambulatorios': Ambulatorios})

def post_form(request):
    form = PostForm()
    return render(request, 'mostambulatorial/addamb.html', {'form': form})

def post_alter(request): 
    return render(request, 'mostambulatorial/alterdados.html', {'Ambulatorios': Ambulatorios})