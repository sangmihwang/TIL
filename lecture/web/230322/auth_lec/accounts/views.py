from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.

def login(request):
    if request.method == 'POST':
        # 로그인 로직
        # 1. form으로 데이터를 받아줌
        form = AuthenticationForm(request, request.POST)
        
        # 2. 유효성 검사
        if form.is_valid():
            
            #3. 로그인
            auth_login(request, form.get_user())
            # 4. index 화면으로 리다이렉션
            # response = redirect('articles:index')
            # response.set_cookie('message', '내가만든쿠키')
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {'form' : form}
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')