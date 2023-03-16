from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

def throw(request):
    return render(request, 'myapps/throw.html')

def catch(request):
    # request : WSGIRequest 객체
    # request.GET : 사전형 자료형
    # 딕셔너리['키값']
    # 딕셔너리.get('키값') -> 키값이 없을 떄 None을 반환
    # 사용자 정보 숨기기 위해 POST로 받아줌
    message = request.POST.get('data')

    context = {
        'message':message
    }
    return render(request, 'myapps/catch.html', context)

def articles(request):
    # 전체 조회
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'myapps/articles.html', context) 

def create(request):
    return render(request, 'myapps/create.html')

# 실제로 데이터를 DB에 저장
def new(request):
    # 데이터 받아오기
    title = request.POST.get('title')
    content = request.POST.get('content')

    # DB에 저장
    Article.objects.create(title=title, content=content)

    # 생성 후 전체 목록 리스트로 가야함
    
    return redirect('myapps:articles')