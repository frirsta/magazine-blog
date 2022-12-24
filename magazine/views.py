from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, LoginForm, ProfileForm
from django.urls import reverse_lazy
from .models import Post, User, Profile


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
    success_url = reverse_lazy('magazine:login')
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
def profile_page(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    return render(request, 'users/profile.html', {'profile': profile, 'user': user})


# Rouizi
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.user.username, request.POST, request.FILES)
        if form.is_valid():
            bio = form.cleaned_data["bio"]
            username = form.cleaned_data["username"]
            image = form.cleaned_data["image"]

            user = User.objects.get(id=request.user.id)
            profile = Profile.objects.get(user=user)
            user.username = username
            user.save()
            profile.bio = bio
            if image:
                profile.image = image
            profile.save()
            return redirect("magazine:profile", username=user.username)
    else:
        form = ProfileForm(request.user.username)
    return render(request, "users/edit_profile.html", {"form": form})
