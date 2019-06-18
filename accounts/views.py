from django.shortcuts import render

# Create your views here.
def post_login(request):
    if request.method == "POST":
        form = Medico(data=request.POST)
        if form.is_valid():
            return redirect('http://127.0.0.1:8000/medicos/')
    else: 
        form = Medico()
    return render(request, 'medicos/post_login.html', {'form': form })
