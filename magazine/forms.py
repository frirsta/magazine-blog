from django import forms
from django.contrib.auth.forms import UserCreationForm
from . models import User


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class ProfileForm(forms.Form):
    image = forms.ImageField(required=False)
    bio = forms.CharField(widget=forms.Textarea())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
