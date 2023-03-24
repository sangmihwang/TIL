from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

# Create your views here.

# 전체 영화 데이터 조회 및 index.html 렌더링 (GET)
def index(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'movies/index.html', context)

# 단일 영화 데이터 조회 및 detail.html 렌더링 (GET)
def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {'movie': movie}
    return render(request, 'movies/detail.html', context)


def create(request):

    # 유효성 검증 및 영화 데이터 저장 후 detail.html 리다이렉트 (GET & POST)
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()

    context = {'form': form}
    return render(request, 'movies/create.html', context)


def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect('movies:index')


def update(request, pk):
    movie = Movie.objects.get(pk=pk)

    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', pk=movie.pk)
    else:
        form = MovieForm(instance=movie)

    context = {'form': form, 'movie': movie}
    return render(request, 'movies/update.html', context)