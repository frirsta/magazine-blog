from django.urls import path, reverse_lazy
from . views import SignUpView, HomePageView, loginUser, logoutUser, profile_page
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', loginUser, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('profile/', profile_page, name='profile'),
    path('password_change/', PasswordChangeView.as_view(template_name='users/password_change.html', success_url=reverse_lazy('magazine:password_change_done')), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),name='password_change_done'),

]
