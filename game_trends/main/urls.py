from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('profile', views.profile, name='profile'),
    path('friends', views.friends, name='friends'),
    path('games', views.games, name='games'),
]