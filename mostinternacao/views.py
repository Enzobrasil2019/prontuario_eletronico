from django.shortcuts import render
from django.utils import timezone
from .models import Internacao
from .forms import PostForm
# Create your views here.

def post_list(request): 
    Internacoes = Internacao.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'mostinternacao/mostinter.html', {'Internacoes': Internacoes})

def post_form(request): 
    form = PostForm()
    return render(request, 'mostinternacao/addinter.html', {'form': form})

def post_alter(request): 
    return render(request, 'mostinternacao/alterdados.html', {'Internacoes': Internacoes})

def post_altas(request): 
    Internacoes = Internacao.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'mostinternacao/mostaltas.html', {'Internacoes': Internacoes})