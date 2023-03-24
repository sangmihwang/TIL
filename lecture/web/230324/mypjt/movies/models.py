from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Movie(models.Model):

    title = models.CharField(max_length=20)
    audience = models.IntegerField()

    # input element의 type은 date로 설정
    release_date = models.DateField()

    # select element를 출력해 코미디, 공포, 로맨스 장르 데이터를 선택
    GENRE_CHOICES = (('Comedy','Comedy'),('Thriller','Thriller'),('Romance','Romance'))
    genre = models.CharField(max_length=30, choices=GENRE_CHOICES)

    # I. input element의 type은 number로 설정
    # II. input element attribute 중 step은 0.5, min은 0, max는 5로 설정
    score = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])

    poster_url = models.CharField(max_length=50)
    description = models.TextField()
    actor_image = models.ImageField(blank=True, null=True)