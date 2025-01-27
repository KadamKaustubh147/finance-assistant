from django.shortcuts import render, redirect

from .forms import UserRegistrationForm

from django.contrib.auth import login

def home(request):
    return render(request, 'home.html')

    
def register(request):
    
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save()
            print("User created:", user)
            login(request, user)
            return redirect("home")
        else:
            print(form.errors)
    
    else:   
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {
        "form": form
    })