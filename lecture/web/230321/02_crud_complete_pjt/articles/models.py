from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    author = models.TextField(default='쓰')
    views = models.IntegerField(default=0)
    # upload_to : 미디어 파일 관리를 위해 경로를 추가 설정
    image = models.ImageField(blank=True, upload_to = 'articles/%Y%m%d')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}번째글 - {self.title}'
