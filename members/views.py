from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Members
from django.contrib.auth.decorators import login_required
from .forms import MemberUpdateForm

# Create your views here.
def home(request):
    context = {
        'members': Members.objects.all()
    }
    return render(request, 'members/home.html', context)

@login_required
def profile(request):
    if request.method == "POST":
        m_form = MemberUpdateForm(request.POST, instance=request.user.members)

        if m_form.is_valid():
            m_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        m_form = MemberUpdateForm(instance=request.user.members)



    context = {
        'm_form': m_form
    }

    return render(request, 'members/profile.html', context)

