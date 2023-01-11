from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, LoginForm, ProfileForm, CommentForm
from django.urls import reverse_lazy
from .models import Post, User, Profile, Comment


class HomePageView(ListView):
    """
    This class shows all posts, and adds the newest post on top of the page.
    The posts are ordered by date in decreasing order.
    """

    template_name = 'magazine/home.html'
    queryset = Post.objects.all()
    paginate_by = 6


class PostsView(ListView):
    """
    This class shows all posts, and adds the newest post on top of the page.
    The posts are ordered by date in decreasing order.
    """
    template_name = 'magazine/posts.html'
    queryset = Post.objects.all()


class SignUpView(CreateView):
    """
    This function handles the signup view.
    When user has created their account they get redirected to the login page.
    """
    template_name = 'users/signup.html'
    success_url = reverse_lazy('magazine:login')
    form_class = SignUpForm


def loginUser(request):
    """
    This function handles the login form.
    If the username and password is valid they log in and get redirected to the home page.
    If the username or password is invalid a error message will display on the page.
    """
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
                messages.success(request, 'You have successfully logged in')
                return redirect('magazine:home')
            else:
                messages.warning(request, 'Invalid username or Password')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


def logoutUser(request):
    logout(request)
    return redirect('magazine:login')


# Rouizi
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


# Rouizi
class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        slug = self.kwargs['slug']

        post = get_object_or_404(Post, pk=pk, slug=slug)
        form = CommentForm()
        comments = post.comment_set.all()

        context['comments'] = comments
        context['form'] = form
        context['post'] = Post.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)

        post = Post.objects.filter(id=self.kwargs['pk'])[0]
        comments = post.comment_set.all()

        context['comments'] = comments
        context['form'] = form
        context['post'] = post

        if form.is_valid():

            user = self.request.user
            content = form.cleaned_data['content']

            comment = Comment.objects.create(user=user, content=content, post=post)

            form = CommentForm()
            context['form'] = form
            return self.render_to_response(context=context)

        return self.render_to_response(context=context)


class CreatePost(LoginRequiredMixin, CreateView):
    """
    This class handles the form for creating post.
    Loginrequiredmixin verifies that the current user who has created the post is authenticated.
    """
    model = Post
    fields = ['title', 'article_description', 'content', 'image']
    success_url = reverse_lazy('magazine:home')

    def form_valid(self, form):
        """
        This function saves the post model if the form is valid.
        """
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.slug = slugify(form.cleaned_data['title'])
        self.object.save()
        return super().form_valid(form)


class UpdatePost(LoginRequiredMixin, UpdateView):
    """
    This class handles the view for updating the posts.
    This class allows only the creator of the post to update it.
    """
    model = Post
    fields = ['title', 'article_description', 'content', 'image']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('magazine:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        slug = self.kwargs['slug']
        post = Post.objects.filter(id=self.kwargs['pk'])[0]
        update = True
        context['update'] = 'update'

        return context

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)


class DeletePost(LoginRequiredMixin, DeleteView):
    """
    This class allows the user that has created a post to delete it.
    """
    model = Post
    success_url = reverse_lazy('magazine:home')

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)


class UserPosts(ListView):
    """
    This class allows a user with an account to see all the posts they have made in one place.
    This class adds the newest post on top of the page.
    The posts are ordered by date in decreasing order.
    """
    model = Post
    template_name = 'users/user_posts.html'
    queryset = Post.objects.all()

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user).order_by('-post_created')


class DeleteComment(LoginRequiredMixin, DeleteView):
    """
    This class allows the user that has created a comment to delete it.
    """
    model = Comment
    success_url = reverse_lazy('magazine:home')

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class AdminPage(LoginRequiredMixin, ListView):
    """
    This class adds all the model data in one place for the superuser / Site Owner.
    """

    model = Post
    template_name = 'admin/admin_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.all()
        context['comment'] = Comment.objects.all()
        context['comments_approved'] = Comment.objects.filter(approved=True)
        context['posts'] = Post.objects.all().count()
        context['comments'] = Comment.objects.all().count()
        context['users'] = User.objects.all().count()
        return context