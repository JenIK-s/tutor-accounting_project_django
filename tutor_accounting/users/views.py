from django.shortcuts import render, redirect
from .form import SignInForm
from django.contrib.auth import authenticate, login


def SignIn(request):
    if request.method == 'POST':
        form = SignInForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('accounting:profile')
    else:
        form = SignInForm()
    return render(request, 'users/signin.html', {'form': form})
