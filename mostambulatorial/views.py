from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Ambulatorio
from .forms import PostForm 


# Create your views here.

def post_list(request): 
    qs = Ambulatorio.objects.all()
    nome_do_paciente_contains_query = request.GET.get('nome_do_paciente_contains')

    
    if nome_do_paciente_contains_query != ' ' and nome_do_paciente_contains_query is not None:
        qs = qs.filter(nome_do_paciente__icontains = nome_do_paciente_contains_query)

    context = {
        'queryset': qs
    }

    return render(request, 'mostambulatorial/mostamb.html', context)


def post_form(request): 
     if request.method == "POST":
         form = PostForm(request.POST)
         if form.is_valid():
             amb = form.save(commit=False)
             amb.author = request.user
             amb.published_date = timezone.now()
             amb.save()
             return redirect('http://127.0.0.1:8000/mostpacientes/mostamb/', pk=amb.pk)
     else:
         form = PostForm()
     return render(request, 'mostambulatorial/addamb.html', {'form': form})

 
def post_edit(request, pk):
     amb = get_object_or_404(Post, pk=pk)
     if request.method == "POST":
         form = PostForm(request.POST, instance=amb)
         if form.is_valid():
             amb = form.save(commit=False)
             amb.author = request.user
             amb.published_date = timezone.now()
             amb.save()
             return redirect('post_detail', pk=amb.pk)
     else:
         form = PostForm(instance=amb)
     return render(request, 'blog/alterdados.html', {'form': form})

def post_detail(request, pk):
    Ambulatorio.objects.get(pk=pk)
    Amb = get_object_or_404(Ambulatorio, pk=pk)
    return render(request, 'mostambulatorial/mostdetail.html', {'Amb': Amb})