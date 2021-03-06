from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import reverse

from authentication.forms import LoginForm
from authentication.forms import SignupForm
from twitteruser.models import TwitterUser


def login_view(request):
    if request.method == 'POST':
        data = request.POST
        user = authenticate(
            request,
            username=data.get('username'),
            password=data.get('password'))
        if user:
            login(request, user)
            return HttpResponseRedirect(
                request.GET.get('next', reverse('homepage'))
            )

    form = LoginForm()
    return render(request, 'generic_form.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login_view'))


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            logout(request)
            user = form.save()
            login(request, user)

            return HttpResponseRedirect(reverse('homepage'))

    form = SignupForm()
    return render(request, 'generic_form.html', {'form': form})
