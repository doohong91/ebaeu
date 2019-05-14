from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib.auth.decorators import login_required
from .models import Profile


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            auth_login(request, user)
            return redirect('profile', request.username)
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/form.html', {'form': form, 'name': 'SignUp'})

  
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
        return redirect('profile', request.username)
    else:
        form = AuthenticationForm()
        return render(request, 'accounts/form.html', {'form': form, 'name': 'Login'})


def logout(request):
    auth_logout(request)
    return redirect('api/v1/docs')


@login_required        
def follow(request, user_id):
    person = get_object_or_404(get_user_model(), id=user_id)
    if request.user in person.followers.all():
        person.followers.remove(request.user)
    else :
        person.followers.add(request.user)
    return redirect('profile', person.username)


def profile(request, username):
    profile = get_object_or_404(get_user_model(), username=username)
    return render(request, 'accounts/profile.html', {'profile': profile})


@login_required 
def change_profile(request):
    if request.method == "POST":
        profile_form = ProfileForm(data=request.POST, instance=request.user.profile, files=request.FILES)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile', request.user.username)
    else:
        profile_form = ProfileForm(instance=request.user.profile)
        return render(request, 'accounts/form.html', {'form':profile_form, 'name': 'My Profile'})
