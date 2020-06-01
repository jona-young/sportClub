from django.shortcuts import render
from django.http import HttpResponse
from .models import Members
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    context = {
        'members': Members.objects.all()
    }
    return render(request, 'members/home.html', context)

@login_required
def profile(request):
    return render(request, 'members/profile.html')