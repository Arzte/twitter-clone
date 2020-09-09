from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import View

from authentication.forms import LoginForm
from authentication.forms import SignupForm


class LoginView(View):
    template_name = 'generic_form.html'

    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
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
        return render(request, self.template_name, {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


class SignupView(CreateView):
    template_name = 'generic_form.html'
    form_class = SignupForm
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        login(self.request, form.save())
        return super().form_valid(form)
