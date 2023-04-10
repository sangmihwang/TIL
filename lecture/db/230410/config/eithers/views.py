from django.shortcuts import render, redirect
from .models import Question, Comment
from .forms import QuestionForm, CommentForm

# Create your views here.

def index(request):
    questions = Question.objects.all()
    context = {'questions': questions,}

    return render(request, 'eithers/index.html', context)


def create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('eithers:index')
    
    #  GET 일 때 create.html 을 사용자에게 보여줌
    form = QuestionForm()
    context = {
        'form': form,
    }
    return render(request, 'eithers/create.html', context)


def detail(request, question_pk):
    question = Question.objects.get(pk=question_pk)
    # 역참조
    comments = question.comments.all()
    comment_form = CommentForm()
    context = {
        'question': question,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'eithers/detail.html', context)

# 댓글 생성
def comment(request, question_pk):
    question = Question.objects.get(pk=question_pk)
    
    form = CommentForm(request.POST)
    if form.is_valid():
        # 사용자가 직접 question을 입력하지 않으므로
        # views.py 에서 지정해준 후 저장
        comment = form.save(commit=False)
        comment.question = question
        comment.save()
        
    return redirect('eithers:detail', question_pk)

def random(request):
    # 있는가 없는가
    count = Question.objects.count()
    # 에외처리 먼저
    if count <= 0:
        return redirect('eithers:index')
    
    # 첫번 째 방법 - 가장 쉬운 방법
    question = ra.choice(Question.objects.all())
    return redurect('eithers:detail', question.id)

    # 구글링
    # question = Question.objects.order_by('?').first()
    # return redirect('eithers:detail', question.id)
    
    # 데이터가 적을 떄 일반적으로 사용하는 방법
    # max_id 기준으로 randint 사용하기
    max_id = Question.objects.all().aggregate(max_id=Mac('id'))['max_id']
    question_pk = ra.randint(1, max_id)
    if Question.objects.filter(pk=question_pk).exists():
        return redirect('eithers:detail', question_pk)
    
    return redirect('eithers:detail', question.id)