from django.shortcuts import render
from django.utils import timezone
from .models import Internacao
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.

def post_list(request): 
    qs = Internacao.objects.all()
    nome_do_paciente_contains_query = request.GET.get('nome_do_paciente_contains')

    
    if nome_do_paciente_contains_query != ' ' and nome_do_paciente_contains_query is not None:
        qs = qs.filter(nome_do_paciente__icontains = nome_do_paciente_contains_query)

    context = {
        'queryset': qs
    }

    return render(request, 'mostinternacao/mostinter.html', context)


def post_form(request): 
     if request.method == "POST":
         form = PostForm(request.POST)
         if form.is_valid():
             inter = form.save(commit=False)
             inter.author = request.user
             inter.published_date = timezone.now()
             inter.save()
             return redirect('http://127.0.0.1:8000/mostpacientes/mostinter/', pk=inter.pk)
     else:
         form = PostForm()
     return render(request, 'mostinternacao/addinter.html', {'form': form})

def post_alter(request): 
    return render(request, 'mostinternacao/alterdados.html', {'Internacoes': Internacoes})

def post_altas(request): 
    qs = Internacao.objects.all()
    nome_do_paciente_contains_query = request.GET.get('nome_do_paciente_contains')

    
    if nome_do_paciente_contains_query != ' ' and nome_do_paciente_contains_query is not None:
        qs = qs.filter(nome_do_paciente__icontains = nome_do_paciente_contains_query)

    context = {
        'queryset': qs
    }

    return render(request, 'mostinternacao/mostaltas.html', context )


def post_detail(request, pk):
    post = get_object_or_404(Internacao, pk=pk)
    return render(request, 'mostinternacao/mostdetail.html', {'post': post})


def post_detail(request, pk):
    post = get_object_or_404(Internacao, pk=pk)
    return render(request, 'mostinternacao/mostdetaila.html', {'post': post})