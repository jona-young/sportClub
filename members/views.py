from django.shortcuts import render
from django.http import HttpResponse
from .models import Members

# Create your views here.
def home(request):
    context = {
        'members': Members.objects.all()
    }
    return render(request, 'members/home.html', context)