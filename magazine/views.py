from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from .forms import SignUpForm
from django.urls import reverse_lazy
from .models import Post


class HomePageView(ListView):
    """
    This class shows all posts, and adds the newest post on top of the page.
    The posts are ordered by date in decreasing order.
    """

    template_name = 'magazine/home.html'
    queryset = Post.objects.all()
    paginate_by = 6


class SignUpView(CreateView):
    template_name = 'users/signup.html'
    success_url = reverse_lazy('magazine:home')
    form_class = SignUpForm
    success_message = 'signup success'
