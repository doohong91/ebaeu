'''
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.
def signup(request):
    # 회원가입
    if request.method =="POST":
        # 직접 구현하면 취약성이 발생한다.
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() # form.user_set
            # 가입된 유저의 Profile 레코드 함께 생성
            Profile.objects.create(user=user)
            auth_login(request,user)
            return redirect('posts:list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html',{'form':form})
    
def login(request):
    if request.method == "POST":
        # 실제 로그인(세션에 정보를 넣는다.)
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # user 정보를 가지고 올 땐 get_user를 사용한다.
            auth_login(request,form.get_user())
        return redirect('posts:list')
    else:
        # 유저로부터 username과 비밀번호를 넣는다.
        form = AuthenticationForm()
        return render(request, 'accounts/login.html',{'form':form})

def logout(request):
    auth_logout(request)
    return redirect('posts:list')
    
def profile(request,username):
    # username을 가진 유저의 상세 정보를 보여주는 페이지
    profile = get_object_or_404(get_user_model(),username=username)
    return render(request, 'accounts/profile.html', {'profile': profile})
    
def delete(request):
    # method == POST : 계정을 삭제한다. == DB에서 user를 삭제한다.
    if request.method == "POST":
        request.user.delete()
        return redirect('posts:list')
    # method == GET : 진짜 삭제하시겠습니까?
    else :
        return render(request, 'accounts/delete.html')

# 로그인이 요구되는 페이지며 로그인이 안되어 있으면 로그인하도록 이동한다.        
@login_required        
def follow(request, user_id):
    person = get_object_or_404(get_user_model(),id=user_id)
    # 만약 이미 팔로우한 사람이라면 -> 언팔
    if request.user in person.followers.all():
        person.followers.remove(request.user)
    # 아니면 -> 팔로우
    else :
        person.followers.add(request.user)
        
    return redirect('profile',person.username)
    
@login_required 
def change_profile(request):
    # 프로필 정보 수정
    if request.method == "POST":
        profile_form = ProfileForm(data=request.POST, instance=request.user.profile, files=request.FILES)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile',request.user.username)
    else:
        profile_form = ProfileForm(instance=request.user.profile) # 1:1관계라 바로 접근 가능
        return render(request, 'accounts/change_profile.html', {'profile_form':profile_form})
'''