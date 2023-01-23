from django import forms
from django.contrib.auth.forms import UserCreationForm
from . models import User, Comment, Profile


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(
            attrs={
                'class': 'input-area form-control',
                'placeholder': 'Password', }))
    password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput(
            attrs={
                'class': 'input-area form-control',
                'placeholder': 'Confirm Password',
                }))

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Username',
                'class': 'input-area form-control', }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email',
                'class': 'input-area form-control', })
        }


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'input-area form-control',
            'placeholder': 'Username', }))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'input-area form-control',
            'placeholder': 'Password', }))


class ProfileForm(forms.Form):
    image = forms.ImageField(required=False)
    bio = forms.CharField(
        widget=forms.Textarea(), max_length=500, required=False)
    username = forms.CharField(max_length=100)

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


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'user': forms.TextInput(attrs={
                'placeholder': 'Username',
                'class': 'input-area form-control', }),
            'content': forms.TextInput(attrs={
                'placeholder': 'Comment',
                'class': 'input-area form-control', })
        }
