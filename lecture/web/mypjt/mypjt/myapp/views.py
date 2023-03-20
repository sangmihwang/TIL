from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'myapp/index.html')

# urls.py에 작성한 
def detail(request, number):
    context = {
        'number': number,
    } 
    return render(request, 'myapp/detail.html', context)

def calc(request, num1, num2):
    context = {
        'num1': num1,
        'num2': num2,
        'add': num1 + num2,
        'sub': num1 - num2,
        'multiple': num1 * num2,
        'divide': num1 /num2 if num2 != 0 else '계산할 수 없습니다'
    }
    return render(request, 'myapp/calculator.html', context)