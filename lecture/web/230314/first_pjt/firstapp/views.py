from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Django PJT</h1>")

def templates(request):
    return render(request, 'index.html')

# 브라우저가 화면을 만드는 과정: 렌더링

def templates(request):
    # 모든 앱/templates/ 생략된 주소
    return render(request, 'firstapp/first.html')

def first(request):
    # 변수를 만들고
    # templates으로 전달을 할 수 있다
    # 마지막에 딕셔너리 형태로 전달

    name = '가나다'
    job = '강사'
    # menus = ['햄버거', '제육', '치킨']
    title = 'mY NAME iS EaGle'
    context = {
        'name': name, 
        'job': job,
        # 'menus': menus,
        'title': title
    }
    return render(request, 'firstapp/first.html', context)

def templates(request):
    # 모든 앱/templates/ 생략된 주소
    return render(request, 'firstapp/hwA.html')

def hwA(request):
    menus = ['햄버거']
    return render(request, 'firstapp/hwA.html', {'menu': menus})