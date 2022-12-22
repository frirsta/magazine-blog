from django.urls import path
from . views import SignUpView, HomePageView, login

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', login, name='login'),
]
