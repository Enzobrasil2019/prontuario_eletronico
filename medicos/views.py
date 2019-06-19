 	
from django.utils import timezone
from .models import Medico
from .forms import PostForm
from django.shortcuts import redirect, render, get_object_or_404

# Create your views here.











def post_list(request): 
    qs = Medico.objects.all()
    nome_do_medico_contains_query = request.GET.get('nome_do_medico_contains')

    
    if nome_do_medico_contains_query != ' ' and nome_do_medico_contains_query is not None:
        qs = qs.filter(nome_do_medico__icontains = nome_do_medico_contains_query)

    context = {
        'queryset': qs
    }
    return render(request, 'medicos/post_list.html', context)

def post_form(request): 
     if request.method == "POST":
         form = PostForm(request.POST)
         if form.is_valid():
             med = form.save(commit=False)
             med.author = request.user
             med.published_date = timezone.now()
             med.save()
             return redirect('http://127.0.0.1:8000/mostamb/', pk=post.pk)
     else:
         form = PostForm()
     return render(request, 'medicos/addmed.html', {'form': form})





# Create your views here.
