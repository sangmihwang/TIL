from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.

# login.html 렌더링 & 회원의 로그인 과정 진행
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('movies:index')
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'accounts/login.html', context)


# DB와 클라이언트 쿠키에서 세션 데이터 삭제
def logout(request):
    auth_logout(request)
    return redirect('movies:index')


# signup.html 렌더링
# 유효성 검증 및 회원 데이터 저장 후 index.html 리다이렉트
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('movies:index')
    else:
        form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)


# 수정 대상 회원 데이터 조회 및 update.html 렌더링
# 유효성 검증 및 회원 데이터 수정 후 index.html 리다이렉트
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {'form': form}
    return render(request, 'accounts/update.html', context)


# 단일 회원 데이터 삭제 및 index.html 리다이렉트
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('movies:index')


# change_password.html
# 렌더링 비밀번호 변경 및 index.html 리다이렉트
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('movies:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {'form': form}
    return render(request, 'accounts/change_password.html', context)        