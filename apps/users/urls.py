
from django.urls import path
from .views import LoginView,logout_view



urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    # path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logout_view, name='logout')
    # path('profile/', profile, name='profile'),
]