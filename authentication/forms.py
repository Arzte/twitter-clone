from django import forms

from twitteruser.models import TwitterUser


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = TwitterUser
        fields = ['username', 'password']


class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = TwitterUser
        fields = ['username', 'password', 'first_name', 'last_name', 'email']
