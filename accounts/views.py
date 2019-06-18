from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Create your views here.


def post_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('http://127.0.0.1:8000/pg/')
    else: 
        form = AuthenticationForm()
    return render(request, 'accounts/post_login.html', {'form': form })
