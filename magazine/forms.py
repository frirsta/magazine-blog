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
    bio = forms.CharField(widget=forms.Textarea(), required=False)
    username = forms.CharField()

    def __init__(self, old_username, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.old_username = old_username

    def clean_username(self):
        """
        Displays error if username is taken
        """
        username = self.cleaned_data['username']
        if username != self.old_username:
            if User.objects.filter(username=username).exists():
                raise forms.ValidationError(
                    'Username is taken')
        return username
