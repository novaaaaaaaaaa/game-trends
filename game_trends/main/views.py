from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def profile(request):
    return render(request, 'profile.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def games(request):
    return render(request, 'games.html')

def friends(request):
    return render(request, 'friends.html')