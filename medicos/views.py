 	
from django.utils import timezone
from .models import Medico
from .forms import PostForm
from django.shortcuts import redirect, render

# Create your views here.

def post_list(request): 
    Medicos = Medico.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'medicos/post_list.html', {'Medicos': Medicos})

def post_form(request): 
     if request.method == "POST":
         form = PostForm(request.POST)
         if form.is_valid():
             med = form.save(commit=False)
             med.author = request.user
             med.published_date = timezone.now()
             med.save()
             return redirect('http://127.0.0.1:8000/medicos/', pk=med.pk)
     else:
         form = PostForm()
     return render(request, 'medicos/addmed.html', {'form': form})





# Create your views here.
