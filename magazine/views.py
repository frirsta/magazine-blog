from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import SignUpForm
from django.urls import reverse_lazy
from django.views.generic import ListView


class SignUpView(CreateView):
    template_name = 'users/signup.html'
    success_url = reverse_lazy('magazine/home')
    form_class = SignUpForm
    success_message = 'signup success'
