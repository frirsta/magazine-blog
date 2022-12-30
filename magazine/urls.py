from django.urls import path, reverse_lazy
from . views import SignUpView, HomePageView, loginUser, logoutUser, profile_page, edit_profile, PostsView, PostDetailView, CreatePost, UpdatePost, DeletePost, UserPosts, DeleteComment
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('posts/', PostsView.as_view(), name='posts'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', loginUser, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('profile/<username>/', profile_page, name='profile'),
    path('password_change/', PasswordChangeView.as_view(template_name='users/password_change.html', success_url=reverse_lazy('magazine:password_change_done')), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),name='password_change_done'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('post/<pk>/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('create/', CreatePost.as_view(), name='post_create'),
    path('update/<pk>/<slug:slug>/', UpdatePost.as_view(), name='post_update'),
    path('delete/<pk>/<slug:slug>/', DeletePost.as_view(), name='post_delete'),
    path('profile/posts/<username>', UserPosts.as_view(), name='user_posts'),
    path('delete/comment/<pk>', DeleteComment.as_view(), name='comment_delete'),

]
