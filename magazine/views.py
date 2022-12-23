from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, LoginForm
from django.urls import reverse_lazy
from .models import Post, User, UserProfile


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


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('magazine:home')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('magazine:home')
            else:
                messages.error(request, 'Invalid username or Password')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


def logoutUser(request):
    logout(request)
    return redirect('magazine:login')


@login_required
def profile_page(request):
    return render(request, 'users/profile.html')
