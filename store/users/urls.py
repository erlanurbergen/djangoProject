from django.urls import path, include

from . import views
from django.contrib.auth.decorators import login_required
from .views import UserRegisterView, UserProfileView

app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/<int:pk>/', login_required(UserProfileView.as_view()), name='profile'),
    path('logout/', views.logout, name='logout')
]
