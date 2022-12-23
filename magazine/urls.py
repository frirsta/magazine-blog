from django.urls import path
from . views import SignUpView, HomePageView, loginUser, logoutUser, profile_page

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', loginUser, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('profile/', profile_page, name='user-profile'),
]
