from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm, UserRegisterForm

def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        
        if next:
            return redirect(next)
        
        return redirect('/')

    return render(request, 'registration/login.html', {'form': form})

def register_view(request):
    context = {}
    if request.POST:
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('files')
        else:
            context['registration_form'] = form
    else:
        form = UserRegisterForm()
        context['registration_form'] = form
    return render(request, 'registration/register.html', context)

